<script>
import HeaderNav from "../components/HeaderNav.vue";
import TableUsers from "../components/TableUsers.vue";

export default {
  components: {
    HeaderNav,
    TableUsers,
  },
};
</script>

<template>
  <div class="min-h-screen bg-slate-100">
    <HeaderNav />

    <header class="bg-white shadow">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">
          Usuarios
        </h1>
      </div>
    </header>

    <!-- Content  -->
    <main>
      <section class="w-full mt-10 mb-10">
        <TableUsers />
      </section>
    </main>
  </div>
</template>