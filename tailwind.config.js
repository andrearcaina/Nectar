/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
            "./templates/*.{html,js}",
            "./src/*.{html,js}",
            "./templates/components/*.{html,js}",
            "./templates/pages/*.{html,js}"
          ],
  theme: {
    extend: {},
  },
  plugins: [],
}

