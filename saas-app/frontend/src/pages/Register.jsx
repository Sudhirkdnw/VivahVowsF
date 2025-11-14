import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';

import { register } from '../features/auth/authSlice.js';

function Register() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [form, setForm] = useState({ username: '', email: '', password: '' });

  const handleChange = (event) => {
    setForm((prev) => ({ ...prev, [event.target.name]: event.target.value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await dispatch(register(form));
    navigate('/login');
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-100 to-indigo-100">
      <div className="bg-white shadow-xl rounded-xl p-10 w-full max-w-md space-y-6">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">Create account</h1>
          <p className="text-sm text-slate-500">Join Vivah Vows to plan your journey.</p>
        </div>
        <form className="space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="block text-sm font-medium text-slate-600">Username</label>
            <input
              name="username"
              value={form.username}
              onChange={handleChange}
              className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-slate-600">Email</label>
            <input
              type="email"
              name="email"
              value={form.email}
              onChange={handleChange}
              className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-slate-600">Password</label>
            <input
              type="password"
              name="password"
              value={form.password}
              onChange={handleChange}
              className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
          <button type="submit" className="w-full bg-indigo-500 hover:bg-indigo-600 text-white py-2 rounded-lg font-semibold">
            Register
          </button>
        </form>
        <p className="text-sm text-center text-slate-500">
          Already have an account?{' '}
          <Link className="text-indigo-600 font-medium" to="/login">
            Login
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Register;
