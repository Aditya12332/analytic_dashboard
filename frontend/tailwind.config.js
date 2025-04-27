// tailwind.config.js
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        tealCard: "#3DB2FF",
        blueCard: "#0056D2",
        purpleCard: "#6A4FC4",
        darkBlueCard: "#003E92",
      },
    },
  },
  safelist: [
    "bg-tealCard",
    "bg-blueCard",
    "bg-purpleCard",
    "bg-darkBlueCard",
  ],
  plugins: [],
}
