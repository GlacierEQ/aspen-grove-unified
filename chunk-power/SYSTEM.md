# Chunk Power - Intelligent Batch Processing System

Automated code analysis, improvement, and evolution system for Aspen Grove repositories.

## Architecture

- **Dashboard**: Interactive React app for project selection and batch management
- **Database**: PostgreSQL schema for progress tracking and metrics
- **Processor**: Intelligent batch engine (10 files/batch)
- **Initializer**: Automated GitHub discovery and health scoring

## Usage

1. Open Chunk Power dashboard
2. Select project
3. Initialize batches
4. Process batches sequentially
5. Review improvements and metrics

## Database Schema

- `chunk_power_projects`: Project metadata and health scores
- `chunk_power_batches`: Batch processing history and metrics

## Performance

- 330 total files across 9 repositories
- 33 batches at 10 files per batch
- ~3.3 hours estimated processing time
- Weighted quality scoring with 8-point breakdown
