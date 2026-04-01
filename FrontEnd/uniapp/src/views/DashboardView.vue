<script>
import HeaderNav from "../components/HeaderNav.vue";
import FormUser from "../components/FormUser.vue";
import FormUnit from "../components/FormUnit.vue";
import CardsView from "../components/CardsView.vue";

export default {
  components: {
    HeaderNav,
    FormUser,
    FormUnit,
    CardsView,
  },
  data() {
    return {
      isFormUserVisible: false,
      isFormUnitVisible: false,
    };
  },
  methods: {
    toggleFormUser() {
      this.isFormUserVisible = !this.isFormUserVisible;
    },
    toggleFormUnit() {
      this.isFormUnitVisible = !this.isFormUnitVisible;
    },
  },
};
</script>

<template>
  <div class="min-h-screen bg-slate-100">
    <HeaderNav />

    <header class="bg-white shadow">
      <div class="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">
          Dashboard
        </h1>
        <p class="mt-2 text-lg font-regular tracking-tight text-gray-900">
          Bienvenidos a Uniapp
        </p>
      </div>
    </header>

    <!-- Content -->
    <main>
      <section class="w-full">
        <div class="flex flex-row py-4 px-4 justify-end align-middle gap-4">
          <button
            class="inline-block py-2 px-4 border border-transparent rounded-md text-sm font-bold  leading-5 text-white bg-orange hover:bg-blue focus:outline-none focus:shadow-outline-indigo active:bg-blue transition duration-300 ease-in-out transform hover:scale-105"
            @click.stop="toggleFormUser"
          >
            Crear un usuario
          </button>
          <button
            class="inline-block py-2 px-4 border border-transparent rounded-md text-sm font-bold leading-5 text-white bg-orange hover:bg-blue focus:outline-none focus:shadow-outline-indigo active:bg-blue transition duration-300 ease-in-out transform hover:scale-105"
            @click.stop="toggleFormUnit"
          >
            Crear una Unidad o Proyecto
          </button>
        </div>

        <FormUser v-if="isFormUserVisible" />
        <FormUnit v-if="isFormUnitVisible" />
      </section>

      <!---- Cards -->
      <section class="mt-4 justify-between px-10 py-10">
        <div>
          <CardsView />
        </div>
      </section>
      
    </main>
  </div>
</template>
