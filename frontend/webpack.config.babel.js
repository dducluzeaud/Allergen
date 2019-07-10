import path from 'path';
import HtmlWebpackPlugin from 'html-webpack-plugin';
import Dotenv from 'dotenv-webpack';
import { CleanWebpackPlugin } from 'clean-webpack-plugin';

module.exports = {
  entry: path.join(__dirname, 'src', 'index.js'),
  output: {
    publicPath: '/',
    path: path.join(__dirname, 'build', 'js'),
    filename: 'bundle.js',
  },
  mode: process.env.NODE_ENV || 'development',
  resolve: {
    modules: [path.resolve(__dirname, 'src'), 'node_modules'],
  },
  devServer: {
    contentBase: path.join(__dirname, 'src'),
    historyApiFallback: { disableDotRule: true },
    watchContentBase: true,
    hot: true,
    quiet: true,
  },
  module: {
    rules: [
      {
        // we do not want anything from node_modules to be compiled
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
        resolve: {
          extensions: ['.jsx', '.js'],
        },
      },
      {
        test: /\.html$/,
        use: [
          {
            loader: 'html-loader',
            options: { minimize: true },
          },
        ],
      },
      {
        test: /\.(png|svg|jpg|gif)$/,
        use: ['file-loader'],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: './index.html',
    }),
    new Dotenv(),
    new CleanWebpackPlugin(),
  ],
  watchOptions: {
    poll: true,
  },
};
