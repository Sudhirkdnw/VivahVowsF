import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchAstroSessions } from '../features/astrology/astroSlice.js';

function AstrologyChat() {
  const dispatch = useDispatch();
  const sessions = useSelector((state) => state.astro.sessions);

  useEffect(() => {
    dispatch(fetchAstroSessions());
  }, [dispatch]);

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold text-slate-800">Astro Chat Sessions</h1>
      <div className="space-y-3">
        {sessions.map((session) => (
          <div key={session.id} className="bg-white rounded-xl shadow p-4">
            <h2 className="font-semibold text-slate-700">{session.astrologer?.name}</h2>
            <p className="text-sm text-slate-500">Status: {session.status}</p>
            <p className="text-xs text-slate-400">Scheduled at: {new Date(session.scheduled_at).toLocaleString()}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AstrologyChat;
