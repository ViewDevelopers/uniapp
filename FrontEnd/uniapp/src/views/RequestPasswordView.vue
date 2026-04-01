<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
const submitForm = () => {

  // Redirigir a la ruta "/resetpassword"
  router.push({ name: "Resetpassword" });
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
          Solicitaste un restablecimiento de contraseña
        </h2>
      </div>

      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" @submit.prevent="submitForm">
          <div>
            <label
              for="email"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Correo Electrónico</label
            >
            <div class="mt-2">
              <input
                id="email"
                name="email"
                type="email"
                placeholder="Correo Electrónico"
                autocomplete="email"
                required=""
                v-model="email"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="flex w-full justify-center rounded-md bg-blue px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-orange focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 hover:scale-105 transition-all ease-in-out duration-500"
            >
              Enviar solicitud
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