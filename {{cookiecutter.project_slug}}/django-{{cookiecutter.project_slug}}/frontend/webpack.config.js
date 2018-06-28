const webpack = require('webpack')
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

const production = process.env.NODE_ENV === 'production';

const extractSass = new ExtractTextPlugin({
  filename: '../css/main.css',
});

let plugins = [
  extractSass,
  new webpack.LoaderOptionsPlugin({
    debug: !production,
  }),
];

if (production) {
  plugins = plugins.concat([
    new UglifyJSPlugin(),
  ]);
}

module.exports = {
  entry: ['babel-polyfill', './src/js/index.js'],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'static/js'),
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: extractSass.extract({
          use: [{
            loader: 'css-loader',
            options: {
              minimize: true,
            },
          }, {
            loader: 'sass-loader',
          }],
          fallback: 'style-loader',
        }),
      },
      {
        enforce: 'pre',
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'eslint-loader',
        options: {
          failOnWarning: false,
          failOnError: true,
          configFile: './.eslintrc.json',
        },
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
    ],
  },
  plugins,
};
