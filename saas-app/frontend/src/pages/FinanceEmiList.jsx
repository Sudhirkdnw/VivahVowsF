import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchEmiSchedule, fetchLoanApplications } from '../features/finance/financeSlice.js';

function FinanceEmiList() {
  const dispatch = useDispatch();
  const { applications, emiSchedule } = useSelector((state) => state.finance);
  const [selected, setSelected] = useState('');

  useEffect(() => {
    dispatch(fetchLoanApplications());
  }, [dispatch]);

  useEffect(() => {
    if (selected) {
      dispatch(fetchEmiSchedule(selected));
    }
  }, [dispatch, selected]);

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold text-slate-800">EMI Schedule</h1>
      <select
        value={selected}
        onChange={(event) => setSelected(event.target.value)}
        className="border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
      >
        <option value="">Select loan application</option>
        {applications.map((app) => (
          <option key={app.id} value={app.id}>
            ₹{app.amount} - {app.purpose}
          </option>
        ))}
      </select>
      <div className="space-y-3">
        {emiSchedule.map((emi) => (
          <div key={emi.id} className="bg-white rounded-xl shadow p-4">
            <p className="font-semibold text-slate-700">Installment {emi.installment_number}</p>
            <p className="text-sm text-slate-500">Due: {emi.due_date} • Amount: ₹{emi.amount}</p>
            <p className="text-xs text-slate-400">Paid: {emi.paid ? 'Yes' : 'No'}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default FinanceEmiList;
