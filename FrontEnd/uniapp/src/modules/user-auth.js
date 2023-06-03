// import { ref } from 'vue';
// import Cookies from 'js-cookie';
// import auth from './auth';

// export default function userAuth() {
//     let userLogged = ref(null);
  
//     const login = async (email, password) => {
//         const response = await auth.login(email, password);
//         if (response.status === 200 && response.data) {
//             auth.setUserLogged(response.data);
//             return true;
//         } else {   
//             return { success: false, error: response };
//         }
//     }

//     const logout = async () => {
//         Cookies.remove('userLogged');
//         Cookies.remove('access_token');
//         userLogged.value = null;
//     }

//     const getUserLogged = async () => {
//         const user = await auth.getUserLogged();
//         userLogged.value = user || null;
//       };

//     const validateAuth = async () => {
//         ;
//         const user = await localStorage.getItem('user');
//         return user !== null;
//       };     

//     return {
//         userLogged,
//         login,
//         logout,
//         getUserLogged,
//         validateAuth
//     }
// }