/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./wallpapers_app/templates/**/*.html",
        "./wallpapers_admin/templates/*.html",
],
    theme: {
        extend: {
            colors: {
                "custom-dark-cyan-2": "#388087",
                "custom-dark-cyan-1": "#6FB2B8",
                "custom-cyan": "#BADFE7",
                "custom-green": "#C2EDCF",
                "custom-white": "#F6F7F2",
            },
            aspectRatio: {
                '9/16': '9 / 16',
              },
        },
    },
    plugins: [],
};
