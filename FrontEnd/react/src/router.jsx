import { createBrowserRouter } from "react-router-dom";
import { Navigate } from "react-router-dom";
import DefaultLayout from "./components/DefaultLayout";
import GuestLayout from "./components/GuestLayout";
import Dashboard from "./views/Dashboard";
import Login from "./views/Login";
import Signup from "./views/Signup";


import Reports from "./views/Reports";
import Users from "./views/Users";
import Units from "./views/Units";
import Blog from "./views/Blog";
import Calendar from "./views/Calendar";


const router = createBrowserRouter ([
  {
    path: "/",
    element: <DefaultLayout />,
    children: [
      {
        path: '/dashboard',
        element: <Navigate to="/" />,
      },
      {
        path: "/",
        element: <Dashboard />
      },
      {
        path: "/unidades",
        element: <Units />
      },
      {
        path: "/blog",
        element: <Blog />
      },
      {
        path: "/calendario",
        element: <Calendar />
      },
      {
        path: "/reportes",
        element: <Reports />
      },
      {
        path: "/usuarios",
        element: <Users />
      },
    ],
  },
  {
    path:'/',
    element: <GuestLayout />,
    children : [
      {
        path: '/login',
        element: <Login />
      },
      {
        path: '/signup',
        element: <Signup />
      },
    ],
  }
]);

export default router;