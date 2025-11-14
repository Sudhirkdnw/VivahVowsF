import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

import api from '../../services/api.js';

const initialState = {
  astrologers: [],
  kundliProfiles: [],
  sessions: [],
  status: 'idle',
  error: null,
};

export const fetchAstrologers = createAsyncThunk('astro/fetchAstrologers', async () => {
  const response = await api.get('/astrology/astrologers/');
  return response.data;
});

export const fetchKundliProfiles = createAsyncThunk('astro/fetchKundliProfiles', async () => {
  const response = await api.get('/astrology/kundli-profiles/');
  return response.data;
});

export const fetchAstroSessions = createAsyncThunk('astro/fetchSessions', async () => {
  const response = await api.get('/astrology/chat-sessions/');
  return response.data;
});

const astroSlice = createSlice({
  name: 'astro',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAstrologers.fulfilled, (state, action) => {
        state.astrologers = action.payload.results ?? action.payload;
      })
      .addCase(fetchKundliProfiles.fulfilled, (state, action) => {
        state.kundliProfiles = action.payload.results ?? action.payload;
      })
      .addCase(fetchAstroSessions.fulfilled, (state, action) => {
        state.sessions = action.payload.results ?? action.payload;
      })
      .addMatcher((action) => action.type.startsWith('astro/') && action.type.endsWith('/pending'), (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addMatcher((action) => action.type.startsWith('astro/') && action.type.endsWith('/rejected'), (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addMatcher((action) => action.type.startsWith('astro/') && action.type.endsWith('/fulfilled'), (state) => {
        state.status = 'succeeded';
      });
  },
});

export default astroSlice.reducer;
