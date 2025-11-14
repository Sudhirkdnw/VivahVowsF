import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

import api from '../../services/api.js';

const initialState = {
  threads: [],
  messages: {},
  status: 'idle',
  error: null,
};

export const fetchThreads = createAsyncThunk('chat/fetchThreads', async () => {
  const response = await api.get('/chat/threads/');
  return response.data;
});

export const fetchThreadMessages = createAsyncThunk('chat/fetchMessages', async (threadId) => {
  const response = await api.get('/chat/messages/', { params: { thread_id: threadId } });
  return { threadId, data: response.data };
});

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    appendMessage(state, action) {
      const { threadId, message } = action.payload;
      if (!state.messages[threadId]) {
        state.messages[threadId] = [];
      }
      state.messages[threadId].push(message);
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchThreads.fulfilled, (state, action) => {
        state.threads = action.payload.results ?? action.payload;
      })
      .addCase(fetchThreadMessages.fulfilled, (state, action) => {
        state.messages[action.payload.threadId] = action.payload.data.results ?? action.payload.data;
      })
      .addMatcher((action) => action.type.startsWith('chat/') && action.type.endsWith('/pending'), (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addMatcher((action) => action.type.startsWith('chat/') && action.type.endsWith('/rejected'), (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addMatcher((action) => action.type.startsWith('chat/') && action.type.endsWith('/fulfilled'), (state) => {
        state.status = 'succeeded';
      });
  },
});

export const { appendMessage } = chatSlice.actions;

export default chatSlice.reducer;
