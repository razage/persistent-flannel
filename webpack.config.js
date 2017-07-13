var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: './pf/static/js/index.js',

  output: {
    path: path.resolve(__dirname, 'pf', 'static', 'js'),
    publicPath: '/pf/static/js',
    filename: 'bundle.js'
  },

  module: {
    rules: [
      {
        test: /\.vue$/,
        use: [
          {
            loader: 'vue-loader',
            options: {}
          }
        ]
      },
      {
        test: /\.js$/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: ['es2015']
            }
          }
        ]
      }
    ]
  },

  resolve: {
    alias: {
      'jquery-ui': 'jquery-ui-dist/jquery-ui.js',
      'vue$': 'vue/dist/vue.common.js',
      'vue-clickaway': 'vue-clickaway/dist/vue-clickaway.common.js'
    }
  },

  plugins: [
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery"
    })
  ]
}
