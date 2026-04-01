<script>
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  setup() {
    const router = useRouter();
    const showPassword = ref(false);

    const togglePassword = () => {
      showPassword.value = !showPassword.value;
    };

    const submitForm = () => {
      // Lógica de validación y redirección
      router.push({ name: "Login" });
    };

    return {
      showPassword,
      togglePassword,
      submitForm,
    };
  },
};
</script>

<template>
  <div
    class="flex min-h-full flex-2 flex-col justify-center px-6 py-12 lg:px-8"
  >
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img
        class="mx-auto h-10 w-auto"
        src="../assets/images/logo.svg"
        alt="Uniapp"
      />
      <h2
        class="mt-10 text-center text-lg font-semibold leading-9 tracking-tight text-gray-800"
      >
        Ingresa tus nuevas credenciales
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit.prevent="submitForm">
        <div>
          <label
            for="email"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Tu token de confirmación</label
          >
          <div class="mt-2">
            <input
              id="token"
              name="token"
              type="number"
              placeholder="Mi token"
              v-model="token"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
            />
          </div>

          <label
            for="email"
            class="mt-5 block text-sm font-medium leading-6 text-gray-900"
            >Correo Electrónico</label
          >
          <div class="mt-2">
            <input
              id="email"
              name="email"
              type="email"
              placeholder="Correo Electrónico"
              v-model="email"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Contraseña</label
            >
          </div>
          <div class="mt-2">
            <input
              :type="showPassword ? 'text' : 'password'"
              id="password"
              placeholder="Ingresa tu contraseña"
              :value="password"
              @input="password = $event.target.value"
              :class="{ 'show-password-active': showPassword }"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
            />

            <input
              :type="showPassword ? 'text' : 'password'"
              id="confirmPassword"
              placeholder="Confirma tu contraseña"
              :value="confirmPassword"
              @input="confirmPassword = $event.target.value"
              :class="{ 'show-password-active': showPassword }"
              class="mt-4 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
            />
          </div>
        </div>

        <div class="show-password">
          <input
            type="checkbox"
            id="showPassword"
            class="hidden"
            @change="togglePassword"
          />
          <label
            for="showPassword"
            class="toggle-label relative flex items-center cursor-pointer select-none transition-colors duration-300"
          >
            <div
              :class="[
                'w-12 h-6 rounded-full p-1',
                showPassword ? 'bg-blue' : 'bg-gray-300',
              ]"
            >
              <div
                class="toggle-dot absolute w-4 h-4 rounded-full bg-white transition-transform duration-300"
                :class="{ 'translate-x-6': showPassword }"
              ></div>
            </div>
            <span class="ml-2 text-sm">Mostrar Contraseña</span>
          </label>
        </div>

        <div>
          <button
            type="submit"
            @click="submitForm"
            class="flex w-full justify-center rounded-md bg-blue px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-orange focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 hover:scale-105 transition-all ease-in-out duration-500"
          >
            Restablecer Contraseña
          </button>
        </div>
      </form>

      <p class="mt-10 text-center">
        <a
          href="/"
          class="inline-block py-2 px-4 border border-transparent rounded-md text-sm font-medium leading-5 text-white bg-orange hover:bg-blue focus:outline-none focus:border-indigo-700 focus:shadow-outline-indigo active:bg-indigo-700 transition duration-300 ease-in-out transform hover:scale-105"
        >
          Volver al inicio
        </a>
      </p>
    </div>
  </div>
</template>
