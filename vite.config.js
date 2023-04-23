import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  root: './front/',
  base: process.env.mode === "production" ? "/static/" : "/",
  build: {
    manifest: true,
    modulePreload: false,
    target: 'esnext',
    outDir: '../static/',
    assetsDir: '',
    rollupOptions: {
      input: '/main.jsx',
    },
  }
})

