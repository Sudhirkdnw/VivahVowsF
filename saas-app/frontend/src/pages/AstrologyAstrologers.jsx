import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { fetchAstrologers } from '../features/astrology/astroSlice.js';

function AstrologyAstrologers() {
  const dispatch = useDispatch();
  const astrologers = useSelector((state) => state.astro.astrologers);

  useEffect(() => {
    dispatch(fetchAstrologers());
  }, [dispatch]);

  return (
    <div className="space-y-4">
      <h1 className="text-xl font-semibold text-slate-800">Featured Astrologers</h1>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {astrologers.map((astrologer) => (
          <div key={astrologer.id} className="bg-white rounded-xl shadow p-4">
            <h2 className="font-semibold text-slate-700">{astrologer.name}</h2>
            <p className="text-sm text-slate-500">Experience: {astrologer.experience_years} years</p>
            <p className="text-xs text-slate-400 mt-2">Specialities: {astrologer.specialities?.join(', ')}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AstrologyAstrologers;
