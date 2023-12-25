import { fileURLToPath, URL } from "node:url";

// import { defineConfig } from "vite";
import { defineConfig, loadEnv } from 'vite';
import legacy from "@vitejs/plugin-legacy";
import vue2 from "@vitejs/plugin-vue2";

// export default defineConfig({

//   devServer: {
//     open: process.platform === 'darwin',
//     host: '127.0.0.1',
//     port: 5173,
//     https: true,
//     hotOnly: false,
//     proxy: { 
//       '/api': { target: 'https://api-ts.bank-fclose.com/api/', pathRewrite: { "^/api/": "" } } 
//     }
//   },

//   plugins: [
//     vue2(),
//     legacy({
//       targets: ["ie >= 11"],
//       additionalLegacyPolyfills: ["regenerator-runtime/runtime"],
//     }),
//   ],
//   resolve: {
//     alias: {
//       "@": fileURLToPath(new URL("./src", import.meta.url)),
//     },
//   },

// });


export default defineConfig(({ command, mode }) => {
    process.env = {...process.env, ...loadEnv(mode, process.cwd()) };

    return ({

        env: {
            baseUrl: import.meta.env,
        },

        plugins: [
            vue2(),
            legacy({
                targets: ["ie >= 11"],
                additionalLegacyPolyfills: ["regenerator-runtime/runtime"],
            }),
        ],

        resolve: {
            alias: {
                "@": fileURLToPath(new URL("./src",
                    import.meta.url)),
            },
        },

    });
})