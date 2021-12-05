module.exports = {
  devServer: {
    proxy: {
      "^/api": {
        target: "http://3.15.140.219:8000",
        changeOrigin: true,
        logLevel: "debug",
        pathRewrite: { "^/api": "/api" },
      },
    },
  },
  parallel: true,
  transpileDependencies: ["vuetify"],
};
