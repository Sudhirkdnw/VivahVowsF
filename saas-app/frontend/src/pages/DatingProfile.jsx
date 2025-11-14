import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchDatingProfiles } from '../features/dating/datingSlice.js';
import api from '../services/api.js';

function DatingProfile() {
  const dispatch = useDispatch();
  const profile = useSelector((state) => state.dating.profiles[0]);
  const [form, setForm] = useState({ headline: '', about: '' });
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    dispatch(fetchDatingProfiles());
  }, [dispatch]);

  useEffect(() => {
    if (profile) {
      setForm({ headline: profile.headline || '', about: profile.about || '' });
    }
  }, [profile]);

  const handleChange = (event) => {
    setForm((prev) => ({ ...prev, [event.target.name]: event.target.value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setSaving(true);
    await api.post('/dating/profiles/update_profile/', form);
    setSaving(false);
    dispatch(fetchDatingProfiles());
  };

  return (
    <div className="max-w-2xl space-y-6">
      <h1 className="text-xl font-semibold text-slate-800">Your Dating Profile</h1>
      <form className="bg-white rounded-xl shadow p-6 space-y-4" onSubmit={handleSubmit}>
        <div>
          <label className="block text-sm font-medium text-slate-600">Headline</label>
          <input
            name="headline"
            value={form.headline}
            onChange={handleChange}
            className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-600">About</label>
          <textarea
            name="about"
            value={form.about}
            onChange={handleChange}
            rows={4}
            className="mt-1 w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />
        </div>
        <button
          type="submit"
          className="bg-indigo-500 hover:bg-indigo-600 text-white px-4 py-2 rounded-lg"
          disabled={saving}
        >
          {saving ? 'Saving...' : 'Save profile'}
        </button>
      </form>
      {profile && (
        <div className="bg-white rounded-xl shadow p-6">
          <h2 className="text-lg font-semibold text-slate-700">Preview</h2>
          <p className="text-sm text-slate-500 mt-2">{profile.about}</p>
        </div>
      )}
    </div>
  );
}

export default DatingProfile;
