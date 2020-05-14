
const path = require('path')

module.exports = { 
    "transpileDependencies": [
      "vuetify"
    ],
    outputDir: path.resolve(__dirname, '../backend/public/'),
    devServer: {
        //assetsSubDirectory: 'static',
        //assetsPublicPath: '/',
        proxy: { 
            '/api': { 
                target: 'http://localhost:3000/api',
                changeOrigin: true,
                pathRewrite: { 
                    "^/api" : '' 
                } 
            } 
        }
    },
}