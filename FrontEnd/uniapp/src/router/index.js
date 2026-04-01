import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import ('../views/HomeView.vue'),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import ('../views/LoginView.vue'),
  },
  {
    path: "/nuevopassword",
    name: "Requestnewpassword",
    component: () => import ('../views/RequestPasswordView.vue'),
  },
  {
    path: "/resetpassword",
    name: "Resetpassword",
    component: () => import ('../views/ResetPasswordView.vue'),
  },
  {
    path: "/dashboard",
    name: "Inicio",
    component: () => import ('../views/DashboardView.vue'),
    meta: { requiresAuth: true },
    
  },
  {
    path: "/perfil",
    name: "Perfil",
    component: () => import ('../views/MyProfile.vue'),
    meta: { requiresAuth: true },
    
  },
  {
    path: "/calendario",
    name: "Calendario",
    component: () => import ('../views/CalendarView.vue'),
    meta: { requiresAuth: true },
    
  },
  {
    path: "/usuarios",
    name: "Usuarios",
    component: () => import ('../views/UsersView.vue'),
    meta: { requiresAuth: true },
    
  },
  {
    path: "/unidades",
    name: "Unidades",
    component: () => import ('../views/UnitsView.vue'),
    meta: { requiresAuth: true },
    
  },
  {
    path: "/ajustes",
    name: "Ajustes",
    component: () => import ('../views/SettingsView.vue'),
    meta: { requiresAuth: true },
    
  },
  {
    path: '/:catchAll(.*)',
    name: 'NotFound',
    component: () => import ('../views/NotFoundView.vue'),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

