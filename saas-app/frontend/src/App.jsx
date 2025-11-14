import { Navigate, Route, Routes } from 'react-router-dom';

import Layout from './components/Layout.jsx';
import ProtectedRoute from './components/ProtectedRoute.jsx';
import AstrologyAstrologers from './pages/AstrologyAstrologers.jsx';
import AstrologyChat from './pages/AstrologyChat.jsx';
import AstrologyChatSession from './pages/AstrologyChatSession.jsx';
import AstrologyKundli from './pages/AstrologyKundli.jsx';
import Dashboard from './pages/Dashboard.jsx';
import DatingChat from './pages/DatingChat.jsx';
import DatingMatches from './pages/DatingMatches.jsx';
import DatingProfile from './pages/DatingProfile.jsx';
import FinanceApply from './pages/FinanceApply.jsx';
import FinanceEmiList from './pages/FinanceEmiList.jsx';
import FinanceLoans from './pages/FinanceLoans.jsx';
import Login from './pages/Login.jsx';
import OtpVerify from './pages/OtpVerify.jsx';
import Register from './pages/Register.jsx';
import SubscriptionCurrent from './pages/SubscriptionCurrent.jsx';
import SubscriptionPlans from './pages/SubscriptionPlans.jsx';
import WeddingProjectDetail from './pages/WeddingProjectDetail.jsx';
import WeddingProjects from './pages/WeddingProjects.jsx';

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/otp-verify" element={<OtpVerify />} />

      <Route element={<ProtectedRoute />}>
        <Route element={<Layout />}>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/dashboard" element={<Dashboard />} />

          <Route path="/dating/matches" element={<DatingMatches />} />
          <Route path="/dating/profile" element={<DatingProfile />} />
          <Route path="/dating/chat/:threadId" element={<DatingChat />} />

          <Route path="/astrology/kundli" element={<AstrologyKundli />} />
          <Route path="/astrology/astrologers" element={<AstrologyAstrologers />} />
          <Route path="/astrology/chat" element={<AstrologyChat />} />
          <Route path="/astrology/chat/:sessionId" element={<AstrologyChatSession />} />

          <Route path="/wedding/projects" element={<WeddingProjects />} />
          <Route path="/wedding/projects/:id" element={<WeddingProjectDetail />} />

          <Route path="/finance/loans" element={<FinanceLoans />} />
          <Route path="/finance/loans/apply" element={<FinanceApply />} />
          <Route path="/finance/loans/emi" element={<FinanceEmiList />} />

          <Route path="/subscriptions/plans" element={<SubscriptionPlans />} />
          <Route path="/subscriptions/current" element={<SubscriptionCurrent />} />
        </Route>
      </Route>

      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
}

export default App;
