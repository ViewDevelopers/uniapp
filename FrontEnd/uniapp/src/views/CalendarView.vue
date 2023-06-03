<script>
import HeaderNav from "../components/HeaderNav.vue";
import Calendar from "../components/Calendar.vue";

export default {
  components: {
    HeaderNav,
    Calendar,
  },
};
</script>

<template>
  <div class="min-h-full bg-slate-100">
    <HeaderNav />

    <header class="bg-white shadow">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">
          Calendario
        </h1>
      </div>
    </header>

    <!-- Content  -->
    <main>
      <section class="w-full mt-2 py-5 px-5">
        <Calendar />
      </section>
    </main>
  </div>
</template>