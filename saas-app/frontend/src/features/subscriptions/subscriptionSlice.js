import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

import api from '../../services/api.js';

const initialState = {
  plans: [],
  subscriptions: [],
  payments: [],
  status: 'idle',
  error: null,
};

export const fetchSubscriptionPlans = createAsyncThunk('subscriptions/fetchPlans', async () => {
  const response = await api.get('/subscriptions/plans/');
  return response.data;
});

export const fetchUserSubscriptions = createAsyncThunk('subscriptions/fetchUser', async () => {
  const response = await api.get('/subscriptions/subscriptions/');
  return response.data;
});

export const fetchPayments = createAsyncThunk('subscriptions/fetchPayments', async () => {
  const response = await api.get('/subscriptions/payments/');
  return response.data;
});

const subscriptionSlice = createSlice({
  name: 'subscriptions',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchSubscriptionPlans.fulfilled, (state, action) => {
        state.plans = action.payload.results ?? action.payload;
      })
      .addCase(fetchUserSubscriptions.fulfilled, (state, action) => {
        state.subscriptions = action.payload.results ?? action.payload;
      })
      .addCase(fetchPayments.fulfilled, (state, action) => {
        state.payments = action.payload.results ?? action.payload;
      })
      .addMatcher((action) => action.type.startsWith('subscriptions/') && action.type.endsWith('/pending'), (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addMatcher((action) => action.type.startsWith('subscriptions/') && action.type.endsWith('/rejected'), (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addMatcher((action) => action.type.startsWith('subscriptions/') && action.type.endsWith('/fulfilled'), (state) => {
        state.status = 'succeeded';
      });
  },
});

export default subscriptionSlice.reducer;
