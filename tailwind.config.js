/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: ["./templates/**/*.{html,htm}"],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui'),],
  daisyui: {
    themes: ["light", "dark", "corporate", "cyberpunk"],
  },
}

