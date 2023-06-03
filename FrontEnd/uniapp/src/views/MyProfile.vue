<script>
import { PhotoIcon, UserCircleIcon } from "@heroicons/vue/24/solid";
import HeaderNav from "../components/HeaderNav.vue";

export default {
  components: {
    HeaderNav,
  },
  data() {
    return {
      fullName: "Administrador Uniapp",
      email: "test@test.com",
      username: "AdminUniapp",
    };
  },
};
</script>

<template>
  <div class="min-h-screen bg-white">
    <HeaderNav />

    <div class="min-h-full">
      <!-- Content -->
      <main>
        <div class="mx-auto max-w-7xl py-6 px-6 sm:px-6 lg:px-8">
          <form class="mt-5">
            <div class="space-y-12">
              <div class="pb-12">
                <h2 class="text-2xl font-semibold leading-7 text-gray-900">
                  Mi perfil
                </h2>
                <p class="mt-1 text-sm leading-6 text-gray-600">
                  Esta información se mostrará públicamente, así que ten cuidado
                  con lo que compartas.
                </p>

                <div class="pb-12">
                  <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                    <div class="sm:col-span-full">
                      <label for="first-name" class="block text-sm font-medium leading-6 text-gray-900">
                        Nombre Completo
                      </label>
                      <div class="mt-2">
                        <input
                          type="text"
                          name="first-name"
                          id="first-name"
                          placeholder="Nombre Completo"
                          v-model="fullName"
                          class="block w-full rounded-md border-0 py-1.5 pl-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                        />
                      </div>
                    </div>

                    <div class="sm:col-span-full">
                      <label for="email" class="block text-sm font-medium leading-6 text-gray-900">
                        Correo electrónico
                      </label>
                      <div class="mt-2">
                        <input
                          id="email"
                          name="email"
                          type="email"
                          placeholder="Correo Electrónico"
                          v-model="email"
                          class="block w-full rounded-md border-0 py-1.5 pl-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                        />
                      </div>
                    </div>

                    <div class="sm:col-span-full">
                      <label for="username" class="block text-sm font-medium leading-6 text-gray-900">
                        Nombre de usuario
                      </label>
                      <div class="mt-2">
                        <input
                          type="text"
                          name="username"
                          id="username"
                          placeholder="uniapp.click/adminuniapp"
                          v-model="username"
                          class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6 pl-3"
                        />
                      </div>
                    </div>

                    <div class="mt-5 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                      <div class="col-span-full">
                        <label for="photo" class="block text-sm font-medium leading-6 text-gray-900">
                          Mi imagen
                        </label>
                        <div class="mt-2 flex items-center">
                          <UserCircleIcon class="h-12 w-12 text-gray-300" aria-hidden="true" />
                          <button
                            type="button"
                            class="rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
                          >
                            Cambiar
                          </button>
                        </div>
                      </div>
                    </div>

                    <div class="col-span-full">
                      <label for="cover-photo" class="block text-sm font-medium leading-6 text-gray-900">
                        Carga tus imagenes aquí
                      </label>
                      <div class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10">
                        <div class="text-center">
                          <PhotoIcon class="mx-auto h-12 w-12 text-gray-300" aria-hidden="true" />
                          <div class="mt-4 flex text-sm leading-6 text-gray-600">
                            <label
                              for="file-upload"
                              class="relative cursor-pointer rounded-md bg-white font-semibold text-orange focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-100 focus-within:ring-offset-2 hover:text-bluelight"
                            >
                              <span>Subir un archivo</span>
                              <input
                                id="file-upload"
                                name="file-upload"
                                type="file"
                                class="sr-only"
                              />
                            </label>
                            <p class="pl-1">ó arrastra y suelta aquí...</p>
                          </div>
                          <p class="text-xs leading-5 text-gray-600">
                            PNG, JPG, GIF máximo 10MB
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="mt-6 flex items-center justify-end gap-x-6">
                <button
                  type="button"
                  class="text-sm font-semibold leading-6 text-gray-900"
                >
                  Cancelar
                </button>
                <button
                  type="submit"
                  class="rounded-md bg-blue px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-bluelight focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Guardar información
                </button>
              </div>
            </div>
          </form>
        </div>
      </main>
    </div>
  </div>
</template>
