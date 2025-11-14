import { NavLink } from 'react-router-dom';

const navItems = [
  { to: '/dashboard', label: 'Dashboard' },
  { to: '/dating/matches', label: 'Dating' },
  { to: '/astrology/kundli', label: 'Astrology' },
  { to: '/wedding/projects', label: 'Wedding Planner' },
  { to: '/finance/loans', label: 'Finance' },
  { to: '/subscriptions/plans', label: 'Subscriptions' },
];

function Sidebar() {
  return (
    <aside className="w-64 bg-white shadow-lg hidden md:flex flex-col">
      <div className="p-6 font-bold text-xl border-b">Vivah Vows</div>
      <nav className="flex-1 p-4 space-y-2">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              `block px-3 py-2 rounded-lg font-medium ${
                isActive ? 'bg-indigo-100 text-indigo-600' : 'text-slate-600 hover:bg-slate-100'
              }`
            }
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;
