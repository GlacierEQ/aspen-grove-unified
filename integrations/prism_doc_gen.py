"""APEX Prism Document Generator
Builds court-ready LaTeX from Supabase case_events + Supermemory knowledge.
Output is saved to Supabase documents table for Prism editing.
"""
import os
from supabase import create_client
from integrations.supermemory import SupermemoryClient
from typing import Dict, Any, List

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_SERVICE_KEY"],
)
memory = SupermemoryClient()

LATEX_TEMPLATE = r"""
\documentclass[12pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{times}}
\usepackage{{setspace}}
\doublespacing

\begin{{document}}

\begin{{center}}
\textbf{{IN THE FAMILY COURT OF THE FIRST CIRCUIT}} \\\\
\textbf{{STATE OF HAWAI'I}}
\end{{center}}

\vspace{{1em}}
\noindent
\textbf{{Case No.:}} {case_id} \\\\
\textbf{{Motion:}} {motion_type}

\vspace{{2em}}
\section*{{Introduction}}
{introduction}

\section*{{Factual Background}}
{background}

\section*{{Legal Argument}}
{argument}

\section*{{Conclusion}}
{conclusion}

\vspace{{2em}}
\noindent
Respectfully submitted,\\[2em]
Casey Barton \\\\
Pro Se Litigant, Case {case_id}

\end{{document}}
"""


def generate_motion(case_id: str, motion_type: str) -> Dict[str, Any]:
    """Generate LaTeX motion, save to Supabase, return document record."""

    # Pull case timeline from Supabase
    events_resp = (
        supabase.table("case_events")
        .select("*")
        .eq("case_id", case_id)
        .order("event_date", desc=True)
        .limit(20)
        .execute()
    )

    # Retrieve knowledge from Supermemory
    doc_clauses = memory.retrieve(
        f"{motion_type} motion argument clauses",
        memory_class="document_knowledge",
        limit=5,
    )
    case_facts = memory.retrieve(
        f"case {case_id} key facts",
        memory_class="case_knowledge",
        limit=8,
    )

    # Build sections
    intro = "\n\n".join(f["content"] for f in case_facts[:3]) or "[Introduction to be completed.]"
    background_items = "\n".join(
        f"\\item {e['event_date']}: {e['description']}" for e in events_resp.data[:12]
    )
    background = f"\\begin{{itemize}}\n{background_items}\n\\end{{itemize}}" if background_items else "[Background to be completed.]"
    argument = "\n\n".join(c["content"] for c in doc_clauses) or "[Legal argument to be completed.]"
    conclusion = f"For the foregoing reasons, the Court should grant this Motion for {motion_type.title()}."

    tex_source = LATEX_TEMPLATE.format(
        case_id=case_id,
        motion_type=motion_type.title(),
        introduction=intro,
        background=background,
        argument=argument,
        conclusion=conclusion,
    )

    # Save to Supabase
    doc = (
        supabase.table("documents")
        .insert({
            "title": f"{motion_type.title()} Motion — {case_id}",
            "case_id": case_id,
            "doc_type": "motion",
            "tex_source": tex_source,
            "status": "draft",
        })
        .execute()
        .data[0]
    )

    # Write to Supermemory
    memory.write_document_knowledge(
        doc_id=doc["id"],
        title=doc["title"],
        key_clauses=[c["content"][:120] for c in doc_clauses],
    )

    return {"id": doc["id"], "title": doc["title"], "tex_source": tex_source}


if __name__ == "__main__":
    result = generate_motion(
        case_id="1FDV-23-0001009",
        motion_type="reunification",
    )
    print(f"Document: {result['id']}")
    print(f"Title: {result['title']}")
    print("\n--- LaTeX preview (first 500 chars) ---")
    print(result["tex_source"][:500])
