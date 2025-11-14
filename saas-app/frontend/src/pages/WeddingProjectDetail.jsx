import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import api from '../services/api.js';

const tabs = ['guests', 'tasks', 'budget', 'vendors'];

function WeddingProjectDetail() {
  const { id } = useParams();
  const [project, setProject] = useState(null);
  const [activeTab, setActiveTab] = useState(tabs[0]);

  useEffect(() => {
    async function loadProject() {
      const response = await api.get(`/wedding/projects/${id}/`);
      setProject(response.data);
    }
    loadProject();
  }, [id]);

  if (!project) {
    return <p>Loading...</p>;
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold text-slate-800">{project.name}</h1>
        <p className="text-sm text-slate-500">{project.date} • {project.location}</p>
      </div>
      <div className="bg-white rounded-xl shadow">
        <div className="flex border-b">
          {tabs.map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`flex-1 px-4 py-2 capitalize ${
                activeTab === tab ? 'border-b-2 border-indigo-500 text-indigo-600' : 'text-slate-500'
              }`}
            >
              {tab}
            </button>
          ))}
        </div>
        <div className="p-6 space-y-3">
          {activeTab === 'guests' &&
            project.guests.map((guest) => (
              <div key={guest.id} className="border border-slate-100 rounded-lg p-3">
                <p className="font-semibold text-slate-700">{guest.name}</p>
                <p className="text-xs text-slate-500">RSVP: {guest.rsvp_status}</p>
              </div>
            ))}
          {activeTab === 'tasks' &&
            project.tasks.map((task) => (
              <div key={task.id} className="border border-slate-100 rounded-lg p-3">
                <p className="font-semibold text-slate-700">{task.title}</p>
                <p className="text-xs text-slate-500">Status: {task.status}</p>
              </div>
            ))}
          {activeTab === 'budget' &&
            project.budget_items.map((item) => (
              <div key={item.id} className="border border-slate-100 rounded-lg p-3">
                <p className="font-semibold text-slate-700">{item.category}</p>
                <p className="text-xs text-slate-500">Estimated: ₹{item.estimated_cost} • Actual: ₹{item.actual_cost}</p>
              </div>
            ))}
          {activeTab === 'vendors' &&
            project.vendor_bookings.map((booking) => (
              <div key={booking.id} className="border border-slate-100 rounded-lg p-3">
                <p className="font-semibold text-slate-700">{booking.vendor?.name}</p>
                <p className="text-xs text-slate-500">Status: {booking.status}</p>
              </div>
            ))}
        </div>
      </div>
    </div>
  );
}

export default WeddingProjectDetail;
