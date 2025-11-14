import { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { fetchWeddingProjects } from '../features/wedding/weddingSlice.js';

function WeddingProjects() {
  const dispatch = useDispatch();
  const projects = useSelector((state) => state.wedding.projects);

  useEffect(() => {
    dispatch(fetchWeddingProjects());
  }, [dispatch]);

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-xl font-semibold text-slate-800">Wedding Projects</h1>
        <Link className="text-sm text-indigo-600" to="/wedding/projects/new">
          + New Project
        </Link>
      </div>
      <div className="space-y-3">
        {projects.map((project) => (
          <Link
            key={project.id}
            to={`/wedding/projects/${project.id}`}
            className="block bg-white rounded-xl shadow p-4 hover:ring-2 hover:ring-indigo-200"
          >
            <h2 className="font-semibold text-slate-700">{project.name}</h2>
            <p className="text-sm text-slate-500">{project.date} • {project.location}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default WeddingProjects;
