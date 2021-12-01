module.exports = {
  devServer: {
    proxy: {
      "^/ap": {
        target: "http://localhost:8000",
        changeOrigin: true,
        logLevel: "debug",
        pathRewrite: { "^/api": "/api" },
      },
    },
  },
  transpileDependencies: ["vuetify"],
};
