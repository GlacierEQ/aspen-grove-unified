import React, { useState, useEffect } from 'react';
import { ChevronDown, ChevronUp, Zap, Check, AlertCircle } from 'lucide-react';
import type { ChunkBatch, AspenGroveProject } from '../types';

interface BatchViewerProps {
  project: AspenGroveProject | null;
}

export const BatchViewer: React.FC<BatchViewerProps> = ({ project }) => {
  const [batches, setBatches] = useState<ChunkBatch[]>([]);
  const [expandedBatchId, setExpandedBatchId] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (project) {
      loadBatches();
    }
  }, [project]);

  const loadBatches = async () => {
    if (!project) return;
    try {
      setLoading(true);
      const rows = await window.tasklet.sqlQuery(
        `SELECT * FROM chunk_power_batches WHERE project_id = '${project.id}' ORDER BY batch_number DESC`
      );
      setBatches(rows as unknown as ChunkBatch[]);
    } catch (err) {
      console.error('Failed to load batches:', err);
    } finally {
      setLoading(false);
    }
  };

  if (!project) {
    return (
      <div className="alert alert-info">
        <span>Select a project to view batch processing status</span>
      </div>
    );
  }

  const statusIcon = (status: string) => {
    switch (status) {
      case 'completed':
        return <Check className="text-success" size={16} />;
      case 'processing':
        return <Zap className="text-warning animate-pulse" size={16} />;
      case 'failed':
        return <AlertCircle className="text-error" size={16} />;
      default:
        return <AlertCircle className="text-base-content/40" size={16} />;
    }
  };

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-lg font-semibold">Processing Batches</h2>
        <button
          onClick={loadBatches}
          className="btn btn-sm btn-ghost"
          disabled={loading}
        >
          {loading ? 'Loading...' : 'Refresh'}
        </button>
      </div>

      {batches.length === 0 ? (
        <div className="alert alert-warning">
          <span>No batches yet. Initialize batch processing to get started.</span>
        </div>
      ) : (
        <div className="space-y-2">
          {batches.map((batch) => (
            <div key={batch.id} className="card bg-base-200">
              <button
                onClick={() =>
                  setExpandedBatchId(
                    expandedBatchId === batch.id ? null : batch.id
                  )
                }
                className="card-body p-4 cursor-pointer hover:bg-base-300 transition-colors flex flex-row items-center justify-between"
              >
                <div className="flex items-center gap-3 flex-1">
                  {statusIcon(batch.status)}
                  <div className="text-left">
                    <h3 className="font-semibold text-sm">
                      Batch #{batch.batch_number}
                    </h3>
                    <p className="text-xs text-base-content/60">
                      {batch.file_paths?.length || 0} files
                      {batch.quality_score ? ` • Quality: ${(batch.quality_score * 100).toFixed(0)}%` : ''}
                    </p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`badge ${
                    batch.status === 'completed' ? 'badge-success' :
                    batch.status === 'processing' ? 'badge-warning' :
                    batch.status === 'failed' ? 'badge-error' :
                    'badge-neutral'
                  }`}>
                    {batch.status}
                  </span>
                  {expandedBatchId === batch.id ? (
                    <ChevronUp size={16} />
                  ) : (
                    <ChevronDown size={16} />
                  )}
                </div>
              </button>

              {expandedBatchId === batch.id && (
                <div className="card-body p-4 border-t border-base-300 space-y-3 bg-base-100">
                  {batch.analysis_notes && (
                    <div>
                      <h4 className="text-sm font-semibold mb-1">Analysis</h4>
                      <p className="text-xs text-base-content/70">
                        {batch.analysis_notes}
                      </p>
                    </div>
                  )}

                  {batch.improvements_made && (
                    <div>
                      <h4 className="text-sm font-semibold mb-1">Improvements</h4>
                      <p className="text-xs text-base-content/70">
                        {batch.improvements_made}
                      </p>
                    </div>
                  )}

                  <div className="grid grid-cols-3 gap-2 text-xs">
                    <div className="bg-base-200 p-2 rounded">
                      <div className="text-base-content/60">Quality</div>
                      <div className="font-bold text-lg">
                        {batch.quality_score
                          ? (batch.quality_score * 100).toFixed(0)
                          : '—'}
                        %
                      </div>
                    </div>
                    <div className="bg-base-200 p-2 rounded">
                      <div className="text-base-content/60">Time</div>
                      <div className="font-bold text-lg">
                        {batch.processing_time_minutes || '—'}m
                      </div>
                    </div>
                    <div className="bg-base-200 p-2 rounded">
                      <div className="text-base-content/60">Files</div>
                      <div className="font-bold text-lg">
                        {batch.file_paths?.length || 0}
                      </div>
                    </div>
                  </div>

                  {batch.file_paths && batch.file_paths.length > 0 && (
                    <div>
                      <h4 className="text-sm font-semibold mb-1">Files Processed</h4>
                      <div className="space-y-1">
                        {batch.file_paths.map((filePath, idx) => (
                          <div
                            key={idx}
                            className="text-xs bg-base-200 px-2 py-1 rounded font-mono text-base-content/70"
                          >
                            {filePath}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
