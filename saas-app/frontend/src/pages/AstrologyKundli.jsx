import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchKundliProfiles } from '../features/astrology/astroSlice.js';
import api from '../services/api.js';

function AstrologyKundli() {
  const dispatch = useDispatch();
  const profiles = useSelector((state) => state.astro.kundliProfiles);
  const [form, setForm] = useState({ birth_date: '', birth_time: '', birth_place: '' });

  useEffect(() => {
    dispatch(fetchKundliProfiles());
  }, [dispatch]);

  const handleChange = (event) => {
    setForm((prev) => ({ ...prev, [event.target.name]: event.target.value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    await api.post('/astrology/kundli-profiles/', form);
    setForm({ birth_date: '', birth_time: '', birth_place: '' });
    dispatch(fetchKundliProfiles());
  };

  return (
    <div className="space-y-6 max-w-3xl">
      <h1 className="text-xl font-semibold text-slate-800">Kundli Profiles</h1>
      <form className="bg-white rounded-xl shadow p-6 grid gap-4 md:grid-cols-3" onSubmit={handleSubmit}>
        <input
          name="birth_date"
          type="date"
          value={form.birth_date}
          onChange={handleChange}
          className="border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          required
        />
        <input
          name="birth_time"
          type="time"
          value={form.birth_time}
          onChange={handleChange}
          className="border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          required
        />
        <input
          name="birth_place"
          value={form.birth_place}
          onChange={handleChange}
          placeholder="Birth place"
          className="border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          required
        />
        <button type="submit" className="md:col-span-3 bg-indigo-500 hover:bg-indigo-600 text-white py-2 rounded-lg">
          Create Kundli
        </button>
      </form>
      <div className="space-y-3">
        {profiles.map((profile) => (
          <div key={profile.id} className="bg-white rounded-xl shadow p-4">
            <p className="font-semibold text-slate-700">Born on {profile.birth_date}</p>
            <p className="text-sm text-slate-500">{profile.birth_time} at {profile.birth_place}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AstrologyKundli;
