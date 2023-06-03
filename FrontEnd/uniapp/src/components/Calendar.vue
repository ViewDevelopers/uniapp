<script>
export default {
  data() {
    return {
      year: new Date().getFullYear(),
      month: new Date().getMonth(),
      blankdays: [],
      no_of_days: [],
      events: [],
      showModal: false,
      newEvent: {
        name: "",
        date: "",
        description: "",
      },
    };
  },
  computed: {
    DAYS() {
      return [
        "Domingo",
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
      ];
    },
    MONTH_NAMES() {
      return [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
      ];
    },
  },
  mounted() {
    this.getNoOfDays();
    this.getBlankDays();
  },
  methods: {
    previousMonth() {
      if (this.month === 0) {
        this.month = 11;
        this.year--;
      } else {
        this.month--;
      }
      this.getNoOfDays();
      this.getBlankDays();
    },
    nextMonth() {
      if (this.month === 11) {
        this.month = 0;
        this.year++;
      } else {
        this.month++;
      }
      this.getNoOfDays();
      this.getBlankDays();
    },
    getNoOfDays() {
      const daysInMonth = new Date(this.year, this.month + 1, 0).getDate();
      this.no_of_days = Array.from(
        { length: daysInMonth },
        (_, index) => index + 1
      );
    },
    getBlankDays() {
      const firstDayOfMonth = new Date(this.year, this.month, 1).getDay();
      this.blankdays = Array.from(
        { length: firstDayOfMonth },
        (_, index) => index
      );
    },
    openModal(date) {
      this.showModal = true;
      this.newEvent.date = `${this.year}-${this.month + 1}-${date}`;
    },
    closeModal() {
      this.showModal = false;
      this.newEvent.name = "";
      this.newEvent.date = "";
      this.newEvent.description = "";
    },
    saveEvent() {
      this.events.push({
        name: this.newEvent.name,
        date: this.newEvent.date,
        description: this.newEvent.description,
      });
      this.closeModal();
    },
    eventDateMatches(eventDate, date) {
      const [year, month, day] = eventDate.split("-");
      return this.year == year && this.month + 1 == month && +date == day;
    },
    isCurrentDate(date) {
      const currentDate = new Date();
      return (
        this.year === currentDate.getFullYear() &&
        this.month === currentDate.getMonth() &&
        +date === currentDate.getDate()
      );
    },
  },
};
</script>

<template>
  <div>
    <!-- Calendar -->
    <div class="container mx-auto px-6 py-4 my-auto">
      <div class="bg-white rounded-lg shadow overflow-hidden">
        <!-- Header -->
        <div class="flex items-center justify-between py-2 px-6">
          <div>
            <span class="text-lg font-bold text-gray-800">{{
              MONTH_NAMES[month]
            }}</span>
            <span class="ml-1 text-lg text-gray-600 font-normal">{{
              year
            }}</span>
          </div>
          <div class="border rounded-lg px-1">
            <button
              type="button"
              class="leading-none rounded-lg transition ease-in-out duration-100 inline-flex cursor-pointer hover:bg-gray-200 p-1 items-center"
              :class="{ 'cursor-not-allowed opacity-25': month === 0 }"
              :disabled="month === 0 ? true : false"
              @click="previousMonth"
            >
              <svg
                class="h-6 w-6 text-gray-500 inline-flex leading-none"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 19l-7-7 7-7"
                />
              </svg>
            </button>
            <div class="border-r inline-flex h-6"></div>
            <button
              type="button"
              class="leading-none rounded-lg transition ease-in-out duration-100 inline-flex items-center cursor-pointer hover:bg-gray-200 p-1"
              :class="{ 'cursor-not-allowed opacity-25': month === 11 }"
              :disabled="month === 11 ? true : false"
              @click="nextMonth"
            >
              <svg
                class="h-6 w-6 text-gray-500 inline-flex leading-none"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 5l7 7-7 7"
                />
              </svg>
            </button>
          </div>
        </div>

        <!-- Days -->
        <div class="-mx-1 -mb-1">
          <div class="flex flex-wrap" style="margin-bottom: -40px">
            <template v-for="(day, index) in DAYS" :key="index">
              <div style="width: 14.28%" class="px-2 py-2">
                <div
                  class="text-gray-600 text-sm uppercase tracking-wide font-bold text-center mb-10"
                >
                  {{ day }}
                </div>
              </div>
            </template>
          </div>

          <!-- Number Days -->
          <div class="flex flex-wrap border-t border-l">
            <template v-for="(blankday, index) in blankdays" :key="index">
              <div
                style="
                  width: 14.28%;
                  height: auto;
                  overflow: hidden;
                  overflow-y: auto;
                "
                class="text-center border-r border-b px-4 pt-2"
              ></div>
            </template>
            <template v-for="(date, dateIndex) in no_of_days" :key="dateIndex">
              <div
                style="width: 14.28%; height: 120px"
                class="text-center font-medium text-lg border-r border-b px-4 pt-2"
              >
                <div>
                  <div
                    @click="openModal(date)"
                    class="text-center text-sm mt-1 mb-1 py-2 px-1 rounded-full hover:bg-gray-400 hover:text-white hover:rounded-full cursor-pointer flex items-center justify-center"
                    :class="{
                      'bg-orange text-white font-semibold': isCurrentDate(date),
                    }"
                    :style="{
                      borderRadius: '50%',
                      width: '2.5rem',
                      height: '2.5rem',
                      margin: '0.5rem 4.5rem 0',
                      overflow: 'hidden',
                      overflowY: 'auto',
                      maxHeight: '10rem',
                    }"
                  >
                    {{ date }}
                  </div>

                  <div class="mt-1 overflow-hidden">
                    <template v-for="event in events">
                      <div
                        v-if="eventDateMatches(event.date, date)"
                        class="text-xs font-medium rounded-xl bg-blue text-white px-1 py-1 mb-1"
                      >
                        {{ event.name }}
                      </div>
                    </template>
                  </div>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>

      <!-- Modal for events -->
      <div
        v-if="showModal"
        class="fixed inset-0 flex items-center justify-center bg-slate-50 bg-opacity-90"
      >
        <div class="bg-white rounded-xl shadow-xl p-6 w-96">
          <h2 class="text-xl mb-4 font-semibold">Nuevo evento</h2>
          <div class="mb-4">
            <label class="block mb-1 font-medium text-gray-700"
              >Nombre del evento</label
            >
            <input
              v-model="newEvent.name"
              type="text"
              class="w-full border border-gray-300 rounded px-3 py-2"
              placeholder="Nombre"
            />
          </div>
          <div class="mb-4">
            <label class="block mb-1 font-medium text-gray-700"
              >Descripción</label
            >
            <textarea
              v-model="newEvent.description"
              class="w-full border border-gray-300 rounded px-3 py-2"
              placeholder="Descripción"
            ></textarea>
          </div>
          <div class="text-right">
            <button
              @click="saveEvent"
              class="bg-orange hover:bg-blue text-white font-bold py-2 px-4 rounded"
            >
              Guardar
            </button>
            <button
              @click="closeModal"
              class="ml-2 bg-gray-200 hover:bg-gray-100 text-gray-900 font-bold py-2 px-4 rounded"
            >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
