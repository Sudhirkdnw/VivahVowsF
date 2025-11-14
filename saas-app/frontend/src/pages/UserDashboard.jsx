import React from 'react';

const user = {
  name: 'Sudhir',
  email: 'sudhir@example.com',
  avatarUrl: 'https://ui-avatars.com/api/?name=Sudhir&background=ff6b81&color=fff',
  plan: 'Gold',
  planType: 'Premium Plan',
  planExpiry: 'Expired',
  remainingInterest: 54,
  remainingContactView: 15,
  remainingProfileView: 0,
  galleryUploads: 59,
  isVerified: true,
};

const sidebarItems = [
  { label: 'Dashboard', active: true },
  { label: 'Gallery' },
  { label: 'Happy Story' },
  { label: 'Packages' },
  { label: 'My Wallet' },
  { label: 'Referral System' },
  { label: 'Message' },
  { label: 'Support Ticket' },
  { label: 'My Interest' },
  { label: 'Shortlist' },
  { label: 'Change Password' },
  { label: 'Manage Profile' },
  { label: 'Deactivate Account', variant: 'danger' },
];

const topTabs = [
  { label: 'Dashboard', active: true },
  { label: 'My Profile' },
  { label: 'My Interest' },
  { label: 'Shortlist' },
  { label: 'Messaging' },
  { label: 'Ignored User List' },
  { label: 'Matched Profile' },
  { label: 'Profile Viewers' },
];

const stats = [
  {
    label: 'Remaining Interest',
    value: user.remainingInterest,
    icon: '💖',
  },
  {
    label: 'Remaining Contact View',
    value: user.remainingContactView,
    icon: '📞',
  },
  {
    label: 'Remaining Profile Viewer',
    value: user.remainingProfileView,
    icon: '👀',
  },
  {
    label: 'Gallery Uploads',
    value: user.galleryUploads,
    icon: '🖼️',
  },
];

function SidebarNavItem({ label, active = false, variant = 'default' }) {
  const baseClasses = 'w-full text-left px-4 py-2.5 rounded-xl text-sm font-medium transition-colors';
  const activeClasses = 'bg-rose-100 text-rose-600 shadow-sm';
  const defaultClasses = 'text-slate-600 hover:bg-rose-50 hover:text-rose-500';
  const dangerClasses = 'text-rose-500 hover:bg-rose-100 hover:text-rose-600';

  const classes = [
    baseClasses,
    variant === 'danger' ? dangerClasses : defaultClasses,
    active ? activeClasses : '',
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <button type="button" className={classes}>
      {label}
    </button>
  );
}

function TopTabItem({ label, active = false }) {
  return (
    <button
      type="button"
      className={`px-4 py-2 text-sm font-semibold transition-colors border-b-2 ${
        active
          ? 'text-rose-500 border-rose-400'
          : 'text-slate-500 border-transparent hover:text-rose-500 hover:border-rose-300'
      }`}
    >
      {label}
    </button>
  );
}

function StatCard({ icon, label, value }) {
  return (
    <div className="bg-white rounded-2xl shadow-sm p-6 text-center flex flex-col items-center gap-3">
      <div className="text-4xl">{icon}</div>
      <p className="text-xs uppercase tracking-wide text-slate-500">{label}</p>
      <p className="text-3xl font-semibold text-rose-500">{value}</p>
    </div>
  );
}

function UserDashboard() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-rose-50 via-pink-50 to-rose-100">
      <aside className="fixed inset-y-0 left-0 w-72 bg-white/80 backdrop-blur-lg border-r border-white/40 shadow-xl p-8 flex flex-col">
        <div className="flex flex-col items-center text-center">
          <img
            src={user.avatarUrl}
            alt={user.name}
            className="w-24 h-24 rounded-full border-4 border-white shadow-md object-cover"
          />
          <h2 className="mt-4 text-xl font-semibold text-slate-800">{user.name}</h2>
          <p className="text-sm text-slate-500">{user.email}</p>
          <button className="mt-4 inline-flex items-center justify-center rounded-full bg-gradient-to-r from-rose-500 to-rose-400 px-5 py-2 text-sm font-semibold text-white shadow hover:from-rose-600 hover:to-rose-500 transition">
            Public Profile
          </button>
        </div>

        <nav className="mt-8 space-y-1">
          {sidebarItems.map((item) => (
            <SidebarNavItem key={item.label} {...item} />
          ))}
        </nav>
      </aside>

      <main className="ml-72 flex min-h-screen">
        <div className="w-full p-6 sm:p-10">
          <div className="bg-white/60 backdrop-blur rounded-3xl border border-white/70 shadow-lg p-6 sm:p-8">
            <div className="flex flex-wrap gap-2 border-b border-rose-100 pb-2 mb-6">
              {topTabs.map((tab) => (
                <TopTabItem key={tab.label} {...tab} />
              ))}
            </div>

            <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
              {stats.map((stat) => (
                <StatCard key={stat.label} {...stat} />
              ))}
            </div>

            <div className="mt-8 grid gap-6 xl:grid-cols-[minmax(0,2fr)_minmax(0,1fr)]">
              <section className="bg-white rounded-2xl shadow-sm p-6">
                <header className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
                  <h3 className="text-lg font-semibold text-rose-500">Current Package</h3>
                  <span className="text-sm font-medium text-slate-400">Member since 2023</span>
                </header>

                <div className="mt-6 bg-gradient-to-br from-[#ffe6f0] to-[#ffeef5] rounded-2xl p-6 shadow-inner">
                  <div className="flex flex-col gap-6 md:flex-row md:items-start md:justify-between">
                    <div>
                      <span className="inline-flex items-center rounded-full bg-white/80 px-3 py-1 text-xs font-semibold text-rose-500 shadow-sm">
                        {user.planType}
                      </span>
                      <div className="mt-4 flex items-center gap-3">
                        <span className="text-4xl">🌟</span>
                        <div>
                          <h4 className="text-2xl font-bold text-rose-600">{user.plan}</h4>
                          <p className="text-sm text-slate-500">Perfect for those who want maximum visibility</p>
                        </div>
                      </div>

                      <ul className="mt-5 space-y-2 text-sm text-rose-700">
                        <li className="flex items-center gap-2">
                          <span className="text-rose-400">•</span>
                          50 Express Interests
                        </li>
                        <li className="flex items-center gap-2">
                          <span className="text-rose-400">•</span>
                          60 Gallery Photo Upload
                        </li>
                        <li className="flex items-center gap-2">
                          <span className="text-rose-400">•</span>
                          15 Contact Info Views
                        </li>
                        <li className="flex items-center gap-2">
                          <span className="text-rose-400">•</span>
                          Auto Profile Match
                        </li>
                      </ul>
                    </div>

                    <div className="flex flex-col items-start gap-4 md:items-end">
                      <p className="text-sm font-semibold text-rose-500">
                        Package expiry date: <span className="text-rose-600">{user.planExpiry}</span>
                      </p>
                      <button className="inline-flex items-center justify-center rounded-full bg-gradient-to-r from-rose-500 to-rose-400 px-6 py-2 text-sm font-semibold text-white shadow hover:from-rose-600 hover:to-rose-500 transition">
                        Upgrade Package
                      </button>
                    </div>
                  </div>
                </div>
              </section>

              <aside className="bg-white rounded-2xl shadow-sm p-6 flex flex-col items-center text-center gap-4">
                <div className="w-24 h-24 rounded-full bg-gradient-to-br from-amber-200 via-yellow-200 to-amber-300 flex items-center justify-center text-4xl shadow-inner">
                  ☮️
                </div>
                <h3 className={`text-xl font-bold ${user.isVerified ? 'text-amber-500' : 'text-slate-500'}`}>
                  {user.isVerified ? 'VERIFIED' : 'PENDING VERIFICATION'}
                </h3>
                <p className="text-sm text-slate-500">
                  Your profile has been verified. Keep your partner expectations updated to receive curated matches.
                </p>
                <button className="mt-2 inline-flex items-center justify-center rounded-full border border-amber-400 px-6 py-2 text-sm font-semibold text-amber-500 hover:bg-amber-50 transition">
                  Update Partner Expectations
                </button>
              </aside>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default UserDashboard;
