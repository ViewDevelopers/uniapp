<script>
import { ref } from "vue";
import UpdateUser from "../components/UpdateUser.vue";

export default {
  components: {
    UpdateUser,
  },
  data() {
    return {
      users: [
        {
          id: "1",
          name: "Administrador Uniapp",
          email: "test@test.com",
          rol: "Administrador",
        },
        ...Array.from({ length: 5 }, (_, index) => ({
          id: (index + 2).toString(),
          name: `Usuario ${index + 1}`,
          email: `usuario${index + 1}@example.com`,
          rol: "Encargado",
        })),
      ],
      isUpdateUserVisible: false,
      selectedUser: null,
    };
  },
  methods: {
    editUser(userId) {
      this.selectedUser = this.users.find((user) => user.id === userId);
      this.toggleUpdateUser();
    },
    updateUser(updatedUser) {
      const index = this.users.findIndex((user) => user.id === updatedUser.id);
      if (index !== -1) {
        this.users.splice(index, 1, updatedUser);
      }
      this.toggleUpdateUser();
    },
    deleteUser(userId) {
      const index = this.users.findIndex((user) => user.id === userId);
      if (index !== -1) {
        this.users.splice(index, 1);
      }
    },
    toggleUpdateUser() {
      this.isUpdateUserVisible = !this.isUpdateUserVisible;
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
              Email
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Rol
            </th>
            <th
              class="py-3 px-4 bg-gray-200 font-semibold uppercase text-sm text-gray-600 border-b border-gray-300"
            >
              Acciones
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ user.id }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ user.name }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ user.email }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              {{ user.rol }}
            </td>
            <td
              class="py-3 px-4 border-b border-gray-300 text-center align-middle"
            >
              <button
                class="text-blue hover:text-bluelight font-semibold"
                @click="editUser(user.id)"
              >
                Editar
              </button>

              <UpdateUser
                v-if="isUpdateUserVisible"
                :user="selectedUser"
                @updateUser="updateUser"
                @closeUpdateUser="toggleUpdateUser"
              />

              <button
                class="text-red-500 hover:text-red-700 ml-2 font-semibold"
                @click="deleteUser(user.id)"
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
