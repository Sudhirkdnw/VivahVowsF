import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchSubscriptionPlans } from '../features/subscriptions/subscriptionSlice.js';

function SubscriptionPlans() {
  const dispatch = useDispatch();
  const plans = useSelector((state) => state.subscriptions.plans);

  useEffect(() => {
    dispatch(fetchSubscriptionPlans());
  }, [dispatch]);

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold text-slate-800">Plans</h1>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {plans.map((plan) => (
          <div key={plan.id} className="bg-white rounded-xl shadow p-6">
            <h2 className="text-lg font-semibold text-slate-700">{plan.name}</h2>
            <p className="text-sm text-slate-500">₹{plan.price} / {plan.duration_days} days</p>
            <ul className="mt-3 space-y-1 text-sm text-slate-500">
              {plan.features?.map((feature, index) => (
                <li key={index}>• {feature}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}

export default SubscriptionPlans;
