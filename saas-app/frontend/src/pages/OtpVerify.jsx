import { useState } from 'react';

function OtpVerify() {
  const [otp, setOtp] = useState('');
  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`OTP ${otp} submitted`);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <div className="bg-white shadow-lg rounded-xl p-8 w-full max-w-md">
        <h1 className="text-xl font-semibold text-slate-800 mb-4">Verify your phone</h1>
        <p className="text-sm text-slate-500 mb-4">Enter the OTP sent to your registered mobile number.</p>
        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            value={otp}
            onChange={(event) => setOtp(event.target.value)}
            className="w-full border border-slate-200 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            placeholder="123456"
          />
          <button type="submit" className="w-full bg-indigo-500 hover:bg-indigo-600 text-white py-2 rounded-lg font-semibold">
            Verify
          </button>
        </form>
      </div>
    </div>
  );
}

export default OtpVerify;
