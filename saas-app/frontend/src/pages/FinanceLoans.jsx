import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

import { fetchLoanApplications } from '../features/finance/financeSlice.js';

function FinanceLoans() {
  const dispatch = useDispatch();
  const applications = useSelector((state) => state.finance.applications);

  useEffect(() => {
    dispatch(fetchLoanApplications());
  }, [dispatch]);

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-xl font-semibold text-slate-800">Loan Applications</h1>
        <div className="space-x-3">
          <Link className="text-sm text-indigo-600" to="/finance/loans/emi">
            View EMI schedule
          </Link>
          <Link className="text-sm text-indigo-600" to="/finance/loans/apply">
            Apply for loan
          </Link>
        </div>
      </div>
      <div className="space-y-3">
        {applications.map((app) => (
          <div key={app.id} className="bg-white rounded-xl shadow p-4">
            <h2 className="font-semibold text-slate-700">₹{app.amount}</h2>
            <p className="text-sm text-slate-500">Tenure: {app.tenure_months} months</p>
            <p className="text-xs text-slate-400">Status: {app.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default FinanceLoans;
