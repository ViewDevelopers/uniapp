<script setup>
import { ref } from "vue";
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { UserIcon } from "@heroicons/vue/24/outline";

const open = ref(true);
const showPassword = ref(false);

const togglePassword = () => {
  showPassword.value = !showPassword.value;
};
</script>

<template>
  <TransitionRoot as="template" :show="open">
    <Dialog as="div" class="relative z-10" @close="open = false">
      <TransitionChild
        as="template"
        enter="ease-out duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in duration-200"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
        />
      </TransitionChild>

      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div
          class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
        >
          <TransitionChild
            as="template"
            enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100"
            leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          >
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg"
            >
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div>
                  <div
                    class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-green-100 sm:mx-0 sm:h-10 sm:w-10"
                  >
                    <UserIcon class="h-6 w-6 text-blue" aria-hidden="true" />
                  </div>

                  <!---- Form to create Units  -->
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <DialogTitle
                      as="h3"
                      class="text-base font-semibold leading-6 text-gray-900"
                      >Crear un Usuario</DialogTitle
                    >
                    <div class="mt-2">
                      <form action="" class="w-full">
                        <div class="mb-4">
                          <label
                            for="userName"
                            class="block text-sm font-medium leading-6 text-gray-900"
                            >Nombre del usuario</label
                          >
                          <input
                            id="userName"
                            type="text"
                            placeholder="Nombre del usuario"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          />
                        </div>

                        <div class="mb-4">
                          <label
                            for="userEmail"
                            class="block text-sm font-medium leading-6 text-gray-900"
                            >Correo electrónico</label
                          >
                          <input
                            id="userEmail"
                            type="email"
                            placeholder="Correo electrónico"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          />
                        </div>

                        <div class="mb-4">
                          <label
                            for="userType"
                            class="block text-sm font-medium leading-6 text-gray-900"
                            >Tipo de usuario</label
                          >
                          <select
                            id="userType"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          >
                            <option value="">Seleccionar</option>
                            <option value="administrador">Administrador</option>
                            <option value="encargado">Encargado</option>
                          </select>
                        </div>

                        <div class="mt-2">
                          <div class="flex items-center justify-between">
                            <label
                              for="password"
                              class="block text-sm font-medium leading-6 text-gray-900"
                              >Contraseña</label
                            >
                          </div>
                          <input
                            :type="showPassword ? 'text' : 'password'"
                            id="password"
                            placeholder="Ingresa tu contraseña"
                            :value="password"
                            @input="password = $event.target.value"
                            :class="{ 'show-password-active': showPassword }"
                            autocomplete="current-password"
                            required=""
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          />
                        </div>

                        <div class="show-password mt-4 mb-10">
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

                        
                        <div class="flex justify-end">
                          <button
                            type="button"
                            class="inline-flex justify-center px-4 py-2 text-sm font-medium text-white bg-green-600 border border-transparent rounded-md shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
                            @click="open = false"
                            ref="cancelButtonRef"
                          >
                            Guardar
                          </button>
                          <button
                            type="button"
                            class="inline-flex justify-center px-4 py-2 ml-3 text-sm font-medium text-gray-700 bg-gray-200 border border-transparent rounded-md shadow-sm hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500"
                            @click="open = false"
                            ref="cancelButtonRef"
                          >
                            Cancelar
                          </button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>
