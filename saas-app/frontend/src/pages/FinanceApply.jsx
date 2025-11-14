import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import api from '../services/api.js';

function FinanceApply() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ amount: '', tenure_months: '', purpose: '' });
  const [submitting, setSubmitting] = useState(false);

  const handleChange = (event) => {
    setForm((prev) => ({ ...prev, [event.target.name]: event.target.value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setSubmitting(true);
    await api.post('/finance/loans/', form);
    setSubmitting(false);
    navigate('/finance/loans');
  };

  return (
    <div className="max-w-xl space-y-6">
      <h1 className="text-xl font-semibold text-slate-800">Apply for Loan</h1>
      <form className="bg-white rounded-xl shadow p-6 space-y-4" onSubmit={handleSubmit}>
        <div>
          <label className="block text-sm font-medium text-slate-600">Amount</label>
          <input
            name="amount"
            value={form.amount}
            onChange={handleChange}
            type="number"
            className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-600">Tenure (months)</label>
          <input
            name="tenure_months"
            value={form.tenure_months}
            onChange={handleChange}
            type="number"
            className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-600">Purpose</label>
          <textarea
            name="purpose"
            value={form.purpose}
            onChange={handleChange}
            className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            rows={4}
            required
          />
        </div>
        <button
          type="submit"
          className="bg-indigo-500 hover:bg-indigo-600 text-white px-4 py-2 rounded-lg"
          disabled={submitting}
        >
          {submitting ? 'Submitting...' : 'Submit application'}
        </button>
      </form>
    </div>
  );
}

export default FinanceApply;
