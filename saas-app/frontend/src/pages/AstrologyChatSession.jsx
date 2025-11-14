import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import api from '../services/api.js';

function AstrologyChatSession() {
  const { sessionId } = useParams();
  const [session, setSession] = useState(null);

  useEffect(() => {
    async function loadSession() {
      const response = await api.get(`/astrology/chat-sessions/${sessionId}/`);
      setSession(response.data);
    }
    loadSession();
  }, [sessionId]);

  if (!session) {
    return <p>Loading session...</p>;
  }

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold text-slate-800">Session with {session.astrologer?.name}</h1>
      <div className="bg-white rounded-xl shadow p-6 space-y-2">
        <p className="text-sm text-slate-500">Status: {session.status}</p>
        <p className="text-sm text-slate-500">Scheduled: {new Date(session.scheduled_at).toLocaleString()}</p>
        {session.notes && <p className="text-sm text-slate-500">Notes: {session.notes}</p>}
      </div>
    </div>
  );
}

export default AstrologyChatSession;
