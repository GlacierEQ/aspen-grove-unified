export interface AspenGroveProject {
  id: string;
  repo_name: string;
  owner: string;
  description: string;
  total_files: number;
  processed_files: number;
  status: 'active' | 'paused' | 'completed';
  created_at: string;
  last_updated: string;
}

export interface ChunkBatch {
  id: string;
  project_id: string;
  batch_number: number;
  file_paths: string[];
  status: 'pending' | 'processing' | 'completed' | 'failed';
  analysis_notes: string;
  improvements_made: string;
  quality_score: number;
  processing_time_minutes: number;
  created_at: string;
  completed_at: string | null;
}

export interface ProjectMetrics {
  total_batches: number;
  completed_batches: number;
  avg_quality_score: number;
  total_processing_time: number;
  improvements_summary: string[];
}
