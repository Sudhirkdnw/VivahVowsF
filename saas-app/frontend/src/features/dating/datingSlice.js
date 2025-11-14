import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

import api from '../../services/api.js';

const initialState = {
  profiles: [],
  matches: [],
  likes: [],
  status: 'idle',
  error: null,
};

export const fetchDatingProfiles = createAsyncThunk('dating/fetchProfiles', async () => {
  const response = await api.get('/dating/profiles/', { params: { mine: 'true' } });
  return response.data;
});

export const fetchMatches = createAsyncThunk('dating/fetchMatches', async () => {
  const response = await api.get('/dating/matches/');
  return response.data;
});

export const fetchLikes = createAsyncThunk('dating/fetchLikes', async () => {
  const response = await api.get('/dating/likes/');
  return response.data;
});

export const likeUser = createAsyncThunk('dating/likeUser', async (likedId) => {
  const response = await api.post('/dating/likes/', { liked_id: likedId });
  return response.data;
});

const datingSlice = createSlice({
  name: 'dating',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchDatingProfiles.fulfilled, (state, action) => {
        state.profiles = action.payload.results ?? action.payload;
        state.status = 'succeeded';
      })
      .addCase(fetchMatches.fulfilled, (state, action) => {
        state.matches = action.payload.results ?? action.payload;
      })
      .addCase(fetchLikes.fulfilled, (state, action) => {
        state.likes = action.payload.results ?? action.payload;
      })
      .addCase(likeUser.fulfilled, (state, action) => {
        state.likes.push(action.payload);
      })
      .addMatcher((action) => action.type.startsWith('dating/') && action.type.endsWith('/pending'), (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addMatcher((action) => action.type.startsWith('dating/') && action.type.endsWith('/rejected'), (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      });
  },
});

export default datingSlice.reducer;
