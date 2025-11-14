import { Outlet } from 'react-router-dom';

import Header from './Header.jsx';
import Sidebar from './Sidebar.jsx';

function Layout() {
  return (
    <div className="min-h-screen flex bg-slate-100">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Header />
        <main className="flex-1 overflow-y-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default Layout;
