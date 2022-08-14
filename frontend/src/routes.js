import Login from "./components/login/Login";
import Register from "./components/register/Register";
import Reset from "./components/reset/Reset";
import Dashboard from "./components/dashboard/Dashboard";
import Clone from "./components/clone/Clone";

import Basic from "./pages/Pricing/Basic";
import Corporate from "./pages/Pricing/Corporate";

export const routes = [
    {
        path: "/",
        label: "Login",
        component: Login,
    },
    {
        path: "/register",
        label: "Register",
        component: Register
    },
    {
        path: "/reset",
        label: "Reset",
        component: Reset
    },
    {
        path: "/dashboard",
        label: "Dashboard",
        component: Dashboard
    },
    {
        path: "/clone",
        label: "Clone",
        component: Clone,
        routes: [
            {
              path: "/basic",
              label: "Basic",
              component: Basic
            },
            {
              path: "/corporate",
              label: "Corporate",
              component: Corporate
            }
          ]
    }
];