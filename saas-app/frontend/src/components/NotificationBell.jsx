import { useState } from 'react';

function NotificationBell() {
  const [open, setOpen] = useState(false);
  const notifications = ['Welcome to Vivah Vows!', 'Complete your profile to get better matches.'];

  return (
    <div className="relative">
      <button
        onClick={() => setOpen((prev) => !prev)}
        className="relative text-slate-600 hover:text-indigo-600"
        aria-label="Notifications"
      >
        <span role="img" aria-hidden className="text-xl">
          🔔
        </span>
        <span className="absolute -top-2 -right-1 bg-red-500 text-white text-xs rounded-full px-1">
          {notifications.length}
        </span>
      </button>
      {open && (
        <div className="absolute right-0 mt-2 w-64 bg-white shadow-lg rounded-lg p-4 space-y-2">
          {notifications.map((notification, index) => (
            <div key={index} className="text-sm text-slate-600">
              {notification}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default NotificationBell;
