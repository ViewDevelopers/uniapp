<script>
import UpdateUnit from "../components/UpdateUnit.vue";

export default {
  components: {
    UpdateUnit,
  },
  data() {
    return {
      isUpdateUnitVisible: false,
      cards: [
        {
          id: 1,
          name: "Conjunto Florida 1",
          address: "Cll. 1 # 2 - 3 Medellín - Colombia",
          manager: "Eder Lara",
        },
        // Agrega más tarjetas aquí si es necesario
      ],
    };
  },
  methods: {
    toggleUpdateUnit() {
      this.isUpdateUnitVisible = !this.isUpdateUnitVisible;
    },
    deleteCard(cardId) {
      this.cards = this.cards.filter((card) => card.id !== cardId);
    },
  },
};
</script>

<template>
  <div
    class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6"
  >
    <!---- Card1 -->
    <div
      class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden"
      v-for="card in cards"
      :key="card.id"
    >
      <img
        src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2FzYXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60"
        alt="Casas1"
        class="h-40 w-full object-cover"
      />
      <div class="p-4">
        <h3 class="text-sm font-bold text-gray-800">Conjunto Florida 1</h3>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Dirección:
          <span class="text-gray-700 font-normal"
            >Cll. 1 # 2 - 3 Medellín - Colombia</span
          >
        </p>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Encargado:
          <span class="text-gray-700 font-normal">Eder Lara</span>
        </p>

        <div class="flex justify-end mt-4">
          <button
            class="px-4 py-2 text-sm font-semibold text-white bg-blue rounded hover:bg-bluelight"
            @click.stop="toggleUpdateUnit"
          >
            Editar
          </button>
          <button
            class="ml-2 px-4 py-2 text-sm font-semibold text-white bg-red-500 rounded hover:bg-red-600"
            @click.stop="deleteCard(card.id)"
          >
            Eliminar
          </button>
        </div>
      </div>
    </div>

    <!---- Card2 -->
    <div class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1605146769289-440113cc3d00?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Y2FzYXN8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60"
        alt="Casas2"
        class="h-40 w-full object-cover"
      />
      <div class="p-4">
        <h3 class="text-sm font-bold text-gray-800">
          Conjunto Altos de Cerezos
        </h3>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Dirección:
          <span class="text-gray-700 font-normal"
            >Cll. 1 # 2 - 3 Bogotá - Colombia</span
          >
        </p>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Encargado:
          <span class="text-gray-700 font-normal">Camila Monrroy</span>
        </p>
        <div class="flex justify-end mt-4">
          <button
            class="px-4 py-2 text-sm font-semibold text-white bg-blue rounded hover:bg-bluelight"
          >
            Editar
          </button>
          <button
            class="ml-2 px-4 py-2 text-sm font-semibold text-white bg-red-500 rounded hover:bg-red-600"
          >
            Eliminar
          </button>
        </div>
      </div>
    </div>

    <!---- Card3 -->
    <div class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1568242629525-62b0c3d77fb7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fGNhc2FzfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60"
        alt="Casas3"
        class="h-40 w-full object-cover"
      />
      <div class="p-4">
        <h3 class="text-sm font-bold text-gray-800">Conjunto Monte Carlo 1</h3>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Dirección:
          <span class="text-gray-700 font-normal"
            >Cll. 1 # 2 - 3 Ibagué - Colombia</span
          >
        </p>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Encargado:
          <span class="text-gray-700 font-normal">Omar Torres</span>
        </p>
        <div class="flex justify-end mt-4">
          <button
            class="px-4 py-2 text-sm font-semibold text-white bg-blue rounded hover:bg-bluelight"
          >
            Editar
          </button>
          <button
            class="ml-2 px-4 py-2 text-sm font-semibold text-white bg-red-500 rounded hover:bg-red-600"
          >
            Eliminar
          </button>
        </div>
      </div>
    </div>

    <!---- Card4 -->
    <div class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1619216083420-6e54b895f730?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGNhc2FzfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60"
        alt="Casas4"
        class="h-40 w-full object-cover"
      />
      <div class="p-4">
        <h3 class="text-sm font-bold text-gray-800">
          Conjunto Bello Horizonte 3
        </h3>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Dirección:
          <span class="text-gray-700 font-normal"
            >Cll. 1 # 2 - 3 Cali - Colombia</span
          >
        </p>
        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Encargado:
          <span class="text-gray-700 font-normal">Sebastian Python</span>
        </p>
        <div class="flex justify-end mt-4">
          <button
            class="px-4 py-2 text-sm font-semibold text-white bg-blue rounded hover:bg-bluelight"
          >
            Editar
          </button>
          <button
            class="ml-2 px-4 py-2 text-sm font-semibold text-white bg-red-500 rounded hover:bg-red-600"
          >
            Eliminar
          </button>
        </div>
      </div>
    </div>

    <!---- Card5 -->
    <div class="max-w-sm mx-auto bg-white rounded-lg shadow-md overflow-hidden">
      <img
        src="https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fGNhc2FzfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60"
        alt="Casas5"
        class="h-40 w-full object-cover"
      />
      <div class="p-4">
        <h3 class="text-sm font-bold text-gray-800">Conjunto Tingua Azul</h3>
        <p class="font-semibold mt-2 text-sm">
          Dirección:
          <span class="text-gray-700 font-normal">
            Cll. 1 # 2 - 3 Bucaramanga - Colombia
          </span>
        </p>

        <p class="text-gray-900 font-semibold mt-2 text-sm">
          Encargado:
          <span class="text-gray-700 font-normal">Anddy Python</span>
        </p>
        <div class="flex justify-end mt-4">
          <button
            class="px-4 py-2 text-sm font-semibold text-white bg-blue rounded hover:bg-blue-600 hover:bg-bluelight"
          >
            Editar
          </button>
          <button
            class="ml-2 px-4 py-2 text-sm font-semibold text-white bg-red-500 rounded hover:bg-red-600"
          >
            Eliminar
          </button>
        </div>
      </div>
    </div>

    <UpdateUnit v-if="isUpdateUnitVisible" />
  </div>
</template>
