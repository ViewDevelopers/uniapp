<script>
import { ref } from "vue";
import UpdateUnit from "../components/UpdateUnit.vue";

export default {
  components: {
    UpdateUnit,
  },
  data() {
    return {
      units: [
        {
          id: "1",
          name: "Conjunto Florida 1",
          encargado: "Eder Lara",
          telefono: "1234567",
          direccion: "Cll 1 # 2 - 3",
          ciudad: "Medellín",
        },
        ...Array.from({ length: 5 }, (_, index) => ({
          id: (index + 2).toString(),
          name: `Conjunto de prueba ${index + 1}`,
          encargado: "Eder Lara",
          telefono: "1234567",
          direccion: `Cll. 1${index + 1} # 2 - 3`,
          ciudad: "Barranquilla",
        })),
      ],
      isUpdateUnitVisible: false,
      selectedUnit: null,
    };
  },
  methods: {
    editUnit(unitId) {
      this.selectedUnit = this.units.find((unit) => unit.id === unitId);
      this.toggleUpdateUnit();
    },
    updateUnit(updatedUnit) {
      const index = this.units.findIndex((unit) => unit.id === updatedUnit.id);
      if (index !== -1) {
        this.units.splice(index, 1, updatedUnit.id);
      }
      this.toggleUpdateUnit();
    },
    deleteUnit(unitId) {
      const index = this.units.findIndex((unit) => unit.id === unitId);
      if (index !== -1) {
        this.units.splice(index, 1);
      }
    },
    toggleUpdateUnit() {
      this.isUpdateUnitVisible = !this.isUpdateUnitVisible;
    },
  },
};
</script>


<template>
  <div class="container mx-auto">
    <div class="overflow-x-auto">
      <table class="min-w-full">
        <thead>
          <tr>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              ID
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Nombre
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Encargado
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Teléfono
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Dirección
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Ciudad
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Acciones
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="unit in units" :key="unit.id">
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ unit.id }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ unit.name }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ unit.encargado }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ unit.telefono }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ unit.direccion }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ unit.ciudad }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              <button
                class="text-blue hover:text-bluelight font-semibold"
                @click="editUnit(unit.id)"
              >
                Editar
              </button>

              <UpdateUnit
                v-if="isUpdateUnitVisible"
                :user="selectedUnit"
                @updateUser="updateUnit"
                @closeUpdateUser="toggleUpdateUnit"
              />

              <button
                class="text-red-500 hover:text-red-700 ml-2 font-semibold"
                @click="deleteUnit(unit.id)"
              >
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
