import { configureStore } from '@reduxjs/toolkit';

import authReducer from '../features/auth/authSlice.js';
import datingReducer from '../features/dating/datingSlice.js';
import astroReducer from '../features/astrology/astroSlice.js';
import weddingReducer from '../features/wedding/weddingSlice.js';
import financeReducer from '../features/finance/financeSlice.js';
import subscriptionsReducer from '../features/subscriptions/subscriptionSlice.js';
import chatReducer from '../features/chat/chatSlice.js';

const store = configureStore({
  reducer: {
    auth: authReducer,
    dating: datingReducer,
    astro: astroReducer,
    wedding: weddingReducer,
    finance: financeReducer,
    subscriptions: subscriptionsReducer,
    chat: chatReducer,
  },
});

export default store;
