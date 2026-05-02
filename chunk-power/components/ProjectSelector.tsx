import React, { useState, useEffect } from 'react';
import { Github, Loader } from 'lucide-react';
import type { AspenGroveProject } from '../types';

interface ProjectSelectorProps {
  onProjectSelect: (project: AspenGroveProject) => void;
  selectedProjectId: string | null;
}

export const ProjectSelector: React.FC<ProjectSelectorProps> = ({
  onProjectSelect,
  selectedProjectId,
}) => {
  const [projects, setProjects] = useState<AspenGroveProject[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      setLoading(true);
      setError(null);
      const rows = await window.tasklet.sqlQuery(
        'SELECT * FROM chunk_power_projects ORDER BY last_updated DESC'
      );
      setProjects(rows as unknown as AspenGroveProject[]);
    } catch (err) {
      console.error('Failed to load projects:', err);
      setError('Failed to load Aspen Grove projects');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center p-8">
        <span className="loading loading-spinner loading-lg text-primary" />
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-2 mb-4">
        <Github size={20} />
        <h2 className="text-lg font-semibold">Aspen Grove Projects</h2>
      </div>

      {error && (
        <div className="alert alert-error">
          <span>{error}</span>
        </div>
      )}

      {projects.length === 0 ? (
        <div className="alert alert-info">
          <span>No projects loaded. Initialize from GitHub to get started.</span>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-3">
          {projects.map((project) => (
            <button
              key={project.id}
              onClick={() => onProjectSelect(project)}
              className={`card p-4 text-left transition-all cursor-pointer ${
                selectedProjectId === project.id
                  ? 'bg-primary text-primary-content ring-2 ring-primary'
                  : 'bg-base-200 hover:bg-base-300'
              }`}
            >
              <div className="flex justify-between items-start">
                <div className="flex-1">
                  <h3 className="font-semibold text-sm">{project.repo_name}</h3>
                  <p className={`text-xs ${selectedProjectId === project.id ? 'opacity-90' : 'opacity-60'}`}>
                    {project.description}
                  </p>
                </div>
                <div className="text-right ml-2">
                  <div className="text-sm font-bold">
                    {project.processed_files}/{project.total_files}
                  </div>
                  <progress
                    className="progress progress-primary w-24 mt-1"
                    value={project.processed_files}
                    max={project.total_files}
                  />
                </div>
              </div>
            </button>
          ))}
        </div>
      )}
    </div>
  );
};
