import { document } from 'postcss';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    { path: '/', name: "home", component: () => import('../views/Home.vue') },
    { path: '/login', name: "login", component: () => import('../views/Login.vue') },
    { path: '/campus', name: "campus", component: () => import('../views/Campus.vue'),
      meta: { title: 'Campus', headerTitle: 'Campus', requiresSidebar: true, requiresHeader: true },
      children: [
        { path: 'dashboard', name: "dashboard", component: () => import('../views/Dashboard.vue'), meta: { title: 'Dashboard', headerTitle: 'Dashboard' } },
        { path: 'subjects', name: "subjects", component: () => import('../views/Subjects.vue'), meta: { title: 'Subjects', headerTitle: 'Subjects' } },
        { path: 'homework', name: "homework", component: () => import('../views/Homework.vue'), meta: { title: 'Homework', headerTitle: 'Homework' } },
        { path: 'messages', name: "messages", component: () => import('../views/Messages.vue'), meta: { title: 'Messages', headerTitle: 'Messages' } },
        { path: 'notices', name: "notices", component: () => import('../views/Notices.vue'), meta: { title: 'Notices', headerTitle: 'Notices' } },
        { path: 'profile', name: "profile", component: () => import('../views/UserProfile.vue'), meta: { title: 'Profile', headerTitle: 'Profile' } },
        { path: 'setting', name: "setting", component: () => import('../views/UserSetting.vue'), meta: { title: 'Settings', headerTitle: 'Settings' } },
      ]
    },
    {
      path: '/:catchAll(.*)',
      name: 'NotFound',
      component: () => import('../views/NotFoundView.vue'),
      meta: { title: 'Página No Encontrada' }
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);
  const defaultTitle = 'Online School';

  if (nearestWithTitle) {
    document.title = `${nearestWithTitle.meta.title} | ${defaultTitle}`;
  } else {
    document.title = defaultTitle;
  }
  next();
});

export default router
