import React, { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { Zap } from 'lucide-react';
import { ProjectSelector } from './components/ProjectSelector';
import { BatchViewer } from './components/BatchViewer';
import type { AspenGroveProject } from './types';

const App: React.FC = () => {
  const [selectedProject, setSelectedProject] = useState<AspenGroveProject | null>(null);
  const [initError, setInitError] = useState<string | null>(null);

  useEffect(() => {
    initializeDatabase();
  }, []);

  const initializeDatabase = async () => {
    try {
      // Verify tables exist (created by parent agent)
      await window.tasklet.sqlQuery('SELECT COUNT(*) FROM chunk_power_projects');
    } catch (err) {
      console.error('Database initialization check failed:', err);
      setInitError('Database not initialized. Please run the setup from the main agent.');
    }
  };

  return (
    <div className="min-h-screen bg-base-100 p-6">
      <div className="max-w-4xl mx-auto">
        <div className="flex items-center gap-2 mb-6">
          <Zap className="text-primary" size={28} />
          <h1 className="text-2xl font-bold">Chunk Power</h1>
        </div>

        {initError && (
          <div className="alert alert-error mb-6">
            <span>{initError}</span>
          </div>
        )}

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div>
            <ProjectSelector
              onProjectSelect={setSelectedProject}
              selectedProjectId={selectedProject?.id || null}
            />
          </div>

          <div>
            <BatchViewer project={selectedProject} />
          </div>
        </div>
      </div>
    </div>
  );
};

createRoot(document.getElementById('root')!).render(<App />);
