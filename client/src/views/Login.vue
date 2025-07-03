<script setup>
import { ref } from 'vue';

import OnlineSchoolLogo from '../assets/images/OnlineSchoolLogo.png';

// Form variables
const username = ref('');
const password = ref('');
const rememberMe = ref(false);

// Form functions
const handleLogin = () => {
   console.log('Intentando iniciar sesión con:', {
      username: username.value,
      password: password.value,
      rememberMe: rememberMe.value,
   });

   alert(`Login intentado para: ${username.value}`);

   // Clear fields after submission (optional)
   // username.value = '';
   // password.value = '';
   // rememberMe.value = false;
};

</script>

<template>
   <section class="login-container dark:bg-gray-900">
      <div class="form-container bg-stone-50 rounded-lg shadow-2xl dark:bg-gray-800 dark:border dark:border-gray-700">
         <img class="rounded-lg" alt="online school logo" :src="OnlineSchoolLogo" />
         <div class="form-items">
            <form class="form-items space-y-4 md:space-y-6" @submit.prevent="handleLogin">
               <div class="bg-gray-200 rounded-lg">
                  <input class="w-full" v-model="username" type="text" label="Tu correo electrónico"
                     placeholder="Username" required />
               </div>
               <div class="bg-gray-200 rounded-lg">
                  <input class="w-full" v-model="password" type="password" label="Contraseña" placeholder="••••••••"
                     required />
               </div>
               <div class="flex items-center justify-between">
                  <div class="checkbox-container">
                     <input type="checkbox" id="rememberMe" name="rememberMe" value="Remember me" v-model="rememberMe">
                     <label class="hover:cursor-pointer text-sm font-medium text-primary-600 dark:text-primary-600" for="rememberMe">Remember me</label>
                  </div>
                  <a href="#"
                     class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500">
                     Forgot password?
                  </a>
               </div>
               <button type="submit" size="xl" class="form-button hover:cursor-pointer accent-color">
                  <p class="text-white">
                     Login
                  </p>
               </button>
            </form>
         </div>
      </div>
   </section>
</template>

<style scoped>
</style>
