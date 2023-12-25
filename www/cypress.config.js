const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    specPattern: "cypress/e2e/**/*.{cy,spec}.{js,jsx,ts,tsx}",
    baseUrl: "https://api-ts.bank-fclose.com",
    baseApi: "https://api-ts.bank-fclose.com",
  },
  component: {
    specPattern: "src/**/__tests__/*.{cy,spec}.{js,ts,jsx,tsx}",
    devServer: {
      framework: "vue",
      bundler: "vite",
      open: process.platform === 'darwin',
      host: '0.0.0.0',
      port: 5173,
      https: true,
      hotOnly: false,
    },
  },
});
