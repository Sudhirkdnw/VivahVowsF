import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

import api from '../../services/api.js';

const initialState = {
  applications: [],
  emiSchedule: [],
  status: 'idle',
  error: null,
};

export const fetchLoanApplications = createAsyncThunk('finance/fetchLoans', async () => {
  const response = await api.get('/finance/loans/');
  return response.data;
});

export const fetchEmiSchedule = createAsyncThunk('finance/fetchEmi', async (applicationId) => {
  const response = await api.get('/finance/emi-schedule/', { params: { application_id: applicationId } });
  return response.data;
});

const financeSlice = createSlice({
  name: 'finance',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchLoanApplications.fulfilled, (state, action) => {
        state.applications = action.payload.results ?? action.payload;
      })
      .addCase(fetchEmiSchedule.fulfilled, (state, action) => {
        state.emiSchedule = action.payload.results ?? action.payload;
      })
      .addMatcher((action) => action.type.startsWith('finance/') && action.type.endsWith('/pending'), (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addMatcher((action) => action.type.startsWith('finance/') && action.type.endsWith('/rejected'), (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addMatcher((action) => action.type.startsWith('finance/') && action.type.endsWith('/fulfilled'), (state) => {
        state.status = 'succeeded';
      });
  },
});

export default financeSlice.reducer;
