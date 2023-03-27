import { createRouter, createWebHistory } from "vue-router";
import Auth from "../views/Auth.vue";
import SignUp from "../views/SignUp.vue";
import LogIn from "../views/LogIn.vue";
import ToDoLists from "../views/ToDoLists.vue";
import ToDoList from "../views/ToDoList.vue";

const routes = [
    {
        path: '/',
        name: 'Auth',
        component: Auth
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/log-in',
        name: 'LogIn',
        component: LogIn
    },
    {
        path: '/to-do-lists',
        name: 'ToDoLists',
        component: ToDoLists
    },
    {
        path: '/to-do-lists/:slug',
        name: 'ToDoList',
        component: ToDoList
    }
]

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes,
});
export default router;
