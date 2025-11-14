import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

import { fetchMatches } from '../features/dating/datingSlice.js';

function DatingMatches() {
  const dispatch = useDispatch();
  const matches = useSelector((state) => state.dating.matches);

  useEffect(() => {
    dispatch(fetchMatches());
  }, [dispatch]);

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold text-slate-800">Your Matches</h1>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {matches.map((match) => (
          <div key={match.id} className="bg-white shadow rounded-xl p-4">
            <p className="font-semibold text-slate-700">{match.user_one?.username}</p>
            <p className="text-sm text-slate-500">Matched with {match.user_two?.username}</p>
            <Link className="text-indigo-600 text-sm mt-3 inline-block" to={`/dating/chat/${match.id}`}>
              Open chat
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DatingMatches;
