import { useDispatch, useSelector } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';

import { logout } from '../features/auth/authSlice.js';
import NotificationBell from './NotificationBell.jsx';

function Header() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSelector((state) => state.auth.user);

  const handleLogout = () => {
    dispatch(logout());
    navigate('/login');
  };

  return (
    <header className="h-16 bg-white border-b flex items-center justify-between px-6">
      <div className="md:hidden">
        <Link to="/dashboard" className="text-lg font-semibold">
          Vivah Vows
        </Link>
      </div>
      <div className="flex items-center gap-4">
        <NotificationBell />
        {user ? (
          <div className="flex items-center gap-3">
            <span className="text-sm text-slate-600">Hi, {user.username}</span>
            <button
              onClick={handleLogout}
              className="text-sm bg-indigo-500 hover:bg-indigo-600 text-white px-3 py-1 rounded"
            >
              Logout
            </button>
          </div>
        ) : (
          <Link className="text-sm text-indigo-600" to="/login">
            Login
          </Link>
        )}
      </div>
    </header>
  );
}

export default Header;
