"""APEX MotherDuck ETL
Replicates Supabase operational tables to MotherDuck analytics warehouse.
Run via cron, GitHub Actions Phase 6, or manually.
"""
import os
import duckdb
from datetime import datetime


def run_etl(
    motherduck_token: str = None,
    supabase_db_url: str = None,
):
    md_token = motherduck_token or os.environ["MOTHERDUCK_TOKEN"]
    sb_url = supabase_db_url or os.environ["SUPABASE_DB_URL"]

    print(f"[{datetime.now().isoformat()}] APEX MotherDuck ETL starting...")

    con = duckdb.connect(f"md:?motherduck_token={md_token}")
    con.execute(f"ATTACH '{sb_url}' AS sb (TYPE POSTGRES);")

    steps = [
        # Deployments (90-day rolling)
        (
            "apex_deployments",
            """
            SELECT d.*, r.name repo_name, r.owner repo_owner, r.tier
            FROM sb.deployments d
            LEFT JOIN sb.repos r ON d.repo_id = r.id
            WHERE d.created_at > current_date - INTERVAL '90 days'
            """,
        ),
        # Incidents (HIGH/CRITICAL + last 30 days)
        (
            "apex_incidents",
            """
            SELECT i.*, r.name repo_name
            FROM sb.incident_log i
            LEFT JOIN sb.repos r ON i.repo_id = r.id
            WHERE i.severity IN ('HIGH', 'CRITICAL')
               OR i.created_at > current_date - INTERVAL '30 days'
            """,
        ),
        # Full repo registry
        ("apex_repos", "SELECT * FROM sb.repos"),
        # Case events (last 365 days)
        (
            "apex_case_events",
            "SELECT * FROM sb.case_events WHERE event_date > current_date - INTERVAL '365 days'",
        ),
        # Memory objects (unsynced)
        (
            "apex_memory_objects",
            "SELECT * FROM sb.memory_objects WHERE synced_to_supermemory = true",
        ),
    ]

    for table_name, query in steps:
        print(f"  Syncing {table_name}...", end=" ")
        con.execute(f"CREATE OR REPLACE TABLE {table_name} AS {query}")
        count = con.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        print(f"{count} rows")

    # Analytics views
    print("  Creating analytics views...")
    con.execute("""
        CREATE OR REPLACE VIEW deployment_health AS
        SELECT
            repo_name,
            COUNT(*) total_deploys,
            SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) successful,
            ROUND(100.0 * SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) / COUNT(*), 2) success_rate,
            AVG(build_time_ms) avg_build_ms
        FROM apex_deployments
        WHERE created_at > current_date - INTERVAL '30 days'
        GROUP BY repo_name
        ORDER BY success_rate;
    """)

    con.execute("""
        CREATE OR REPLACE VIEW incident_trends AS
        SELECT
            DATE_TRUNC('day', created_at) AS date,
            severity,
            COUNT(*) incidents,
            SUM(CASE WHEN resolved THEN 1 ELSE 0 END) resolved
        FROM apex_incidents
        WHERE created_at > current_date - INTERVAL '30 days'
        GROUP BY date, severity
        ORDER BY date DESC;
    """)

    con.execute("""
        CREATE OR REPLACE VIEW repo_scorecard AS
        SELECT
            r.name, r.tier, r.language, r.stars,
            COUNT(DISTINCT d.id) deploys_30d,
            COUNT(DISTINCT i.id) incidents_30d,
            r.last_activity
        FROM apex_repos r
        LEFT JOIN apex_deployments d ON r.id = d.repo_id
            AND d.created_at > current_date - INTERVAL '30 days'
        LEFT JOIN apex_incidents i ON r.id = i.repo_id
            AND i.created_at > current_date - INTERVAL '30 days'
        GROUP BY r.id, r.name, r.tier, r.language, r.stars, r.last_activity
        ORDER BY deploys_30d DESC;
    """)

    con.close()
    print(f"[{datetime.now().isoformat()}] ETL complete.")


if __name__ == "__main__":
    run_etl()
