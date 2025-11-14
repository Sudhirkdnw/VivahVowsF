import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

import api from '../../services/api.js';

const initialState = {
  projects: [],
  vendorCategories: [],
  vendors: [],
  status: 'idle',
  error: null,
};

export const fetchWeddingProjects = createAsyncThunk('wedding/fetchProjects', async () => {
  const response = await api.get('/wedding/projects/');
  return response.data;
});

export const fetchVendorCategories = createAsyncThunk('wedding/fetchVendorCategories', async () => {
  const response = await api.get('/wedding/vendor-categories/');
  return response.data;
});

export const fetchVendors = createAsyncThunk('wedding/fetchVendors', async () => {
  const response = await api.get('/wedding/vendors/');
  return response.data;
});

const weddingSlice = createSlice({
  name: 'wedding',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchWeddingProjects.fulfilled, (state, action) => {
        state.projects = action.payload.results ?? action.payload;
      })
      .addCase(fetchVendorCategories.fulfilled, (state, action) => {
        state.vendorCategories = action.payload.results ?? action.payload;
      })
      .addCase(fetchVendors.fulfilled, (state, action) => {
        state.vendors = action.payload.results ?? action.payload;
      })
      .addMatcher((action) => action.type.startsWith('wedding/') && action.type.endsWith('/pending'), (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addMatcher((action) => action.type.startsWith('wedding/') && action.type.endsWith('/rejected'), (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addMatcher((action) => action.type.startsWith('wedding/') && action.type.endsWith('/fulfilled'), (state) => {
        state.status = 'succeeded';
      });
  },
});

export default weddingSlice.reducer;
