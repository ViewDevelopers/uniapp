<script setup>
import { ref } from "vue";
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { BuildingOffice2Icon } from "@heroicons/vue/24/outline";

const open = ref(true);
const unitName = ref("Conjunto Florida 1");
const unitAddress = ref("test@test.com");
const unitManager = ref("Eder Lara");
const unitPhone = ref("1234567");
const unitInfo = ref("");

const saveUnit = () => {
  // Lógica para guardar la unidad
  console.log("Guardar unidad:", {
    unitName: unitName.value,
    unitAddress: unitAddress.value,
    unitManager: unitManager.value,
    unitPhone: unitPhone.value,
    unitInfo: unitInfo.value,
  });
  open.value = false; // Cerrar el diálogo después de guardar
};

const cancelCreation = () => {
  open.value = false; // Cerrar el diálogo sin guardar
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
                    <BuildingOffice2Icon
                      class="h-6 w-6 text-blue"
                      aria-hidden="true"
                    />
                  </div>

                  <!---- Form to create Units  -->
                  <div class="mt-3 text-center sm:ml-4 sm:mt-0 sm:text-left">
                    <DialogTitle
                      as="h3"
                      class="text-base font-semibold leading-6 text-gray-900"
                      >Actualiza una Unidad</DialogTitle
                    >
                    <div class="mt-2">
                      <form action="" class="w-full">
                        <div class="mb-4">
                          <label
                            for="unitName"
                            class="block text-sm font-medium text-gray-700"
                            >Nombre de la Unidad</label
                          >
                          <input
                            id="unitName"
                            type="text"
                            v-model="unitName"
                            placeholder="Nombre de la Unidad"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          />
                        </div>
                        <div class="mb-4">
                          <label
                            for="unitAddress"
                            class="block text-sm font-medium text-gray-700"
                            >Dirección</label
                          >
                          <input
                            id="unitAddress"
                            type="text"
                            v-model="unitAddress"
                            placeholder="Direccion de la Unidad"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          />
                        </div>
                        <div class="mb-4">
                          <label
                            for="unitManager"
                            class="block text-sm font-medium text-gray-700"
                            >Encargado</label
                          >
                          <input
                            id="unitManager"
                            type="text"
                            v-model="unitManager"
                            placeholder="Nombre del encargado"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          />
                        </div>
                        <div class="mb-4">
                          <label
                            for="unitPhone"
                            class="block text-sm font-medium text-gray-700"
                            >Teléfono de contacto</label
                          >
                          <input
                            id="unitPhone"
                            type="text"
                            v-model="unitPhone"
                            placeholder="Teléfono de contacto"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          />
                        </div>
                        <div class="mb-4">
                          <label
                            for="unitInfo"
                            class="block text-sm font-medium text-gray-700"
                            >Información Adicional</label
                          >
                          <textarea
                            id="unitInfo"
                            v-model="unitInfo"
                            placeholder="Escribe información Adicional..."
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 pl-3 focus:ring-2 focus:ring-inset focus:ring-indigo-100 sm:text-sm sm:leading-6"
                          ></textarea>
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
