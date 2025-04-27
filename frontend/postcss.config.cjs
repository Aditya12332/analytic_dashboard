module.exports = {
  plugins: [
    require('@tailwindcss/postcss'), // use the separate postcss package for tailwind
    require('autoprefixer'), // you can keep autoprefixer if you want it
  ],
};
