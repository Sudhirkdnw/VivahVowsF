import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchDatingProfiles, fetchMatches } from '../features/dating/datingSlice.js';
import { fetchWeddingProjects } from '../features/wedding/weddingSlice.js';
import { fetchLoanApplications } from '../features/finance/financeSlice.js';

function Dashboard() {
  const dispatch = useDispatch();
  const dating = useSelector((state) => state.dating);
  const wedding = useSelector((state) => state.wedding);
  const finance = useSelector((state) => state.finance);

  useEffect(() => {
    dispatch(fetchDatingProfiles());
    dispatch(fetchMatches());
    dispatch(fetchWeddingProjects());
    dispatch(fetchLoanApplications());
  }, [dispatch]);

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold text-slate-800">Your Journey Overview</h1>
      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-sm text-slate-500">Matches</h2>
          <p className="text-3xl font-bold text-indigo-600">{dating.matches.length}</p>
        </div>
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-sm text-slate-500">Profiles</h2>
          <p className="text-3xl font-bold text-indigo-600">{dating.profiles.length}</p>
        </div>
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-sm text-slate-500">Wedding Projects</h2>
          <p className="text-3xl font-bold text-indigo-600">{wedding.projects.length}</p>
        </div>
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-sm text-slate-500">Loan Applications</h2>
          <p className="text-3xl font-bold text-indigo-600">{finance.applications.length}</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
