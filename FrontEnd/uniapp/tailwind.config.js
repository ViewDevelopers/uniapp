const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // Puedes cambiarlo a 'class' o 'media' según tus necesidades
  theme: {
    extend: {
      colors: {
        blue: "#304BA8",
        bluelight: "#4f6ccc",
        orange: "#FD7E14",
        orangelight: "#c97636",
      },
      fontFamily: {
        sans: ["Montserrat", ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
