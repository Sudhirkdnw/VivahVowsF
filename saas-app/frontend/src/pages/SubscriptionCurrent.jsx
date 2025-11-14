import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchPayments, fetchUserSubscriptions } from '../features/subscriptions/subscriptionSlice.js';

function SubscriptionCurrent() {
  const dispatch = useDispatch();
  const { subscriptions, payments } = useSelector((state) => state.subscriptions);

  useEffect(() => {
    dispatch(fetchUserSubscriptions());
    dispatch(fetchPayments());
  }, [dispatch]);

  const active = subscriptions.filter((subscription) => subscription.is_active);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-xl font-semibold text-slate-800">Current Plan</h1>
        {active.length ? (
          active.map((subscription) => (
            <div key={subscription.id} className="bg-white rounded-xl shadow p-6 mt-3">
              <h2 className="text-lg font-semibold text-slate-700">{subscription.plan?.name}</h2>
              <p className="text-sm text-slate-500">Valid until {subscription.end_date}</p>
            </div>
          ))
        ) : (
          <p className="text-sm text-slate-500">No active subscription.</p>
        )}
      </div>
      <div>
        <h2 className="text-lg font-semibold text-slate-800">Payment History</h2>
        <div className="space-y-3 mt-3">
          {payments.map((payment) => (
            <div key={payment.id} className="bg-white rounded-xl shadow p-4">
              <p className="font-semibold text-slate-700">₹{payment.amount}</p>
              <p className="text-sm text-slate-500">{new Date(payment.paid_at).toLocaleString()}</p>
              <p className="text-xs text-slate-400">Transaction: {payment.transaction_id}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default SubscriptionCurrent;
