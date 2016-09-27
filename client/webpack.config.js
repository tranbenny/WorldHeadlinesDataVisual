var path = require('path');
var webpack = require('webpack');

// PLUGINS
var HtmlWebpackPlugin = require('html-webpack-plugin');
var CommonsPlugin = require('webpack/lib/optimize/CommonsChunkPlugin');

var config = {
	cache: true,
	debug: true,
	devtool: 'eval',
	watch: false, 
	entry: {
		app : './src/app.js'
	},
	output: {
		// example:
		path: path.resolve('dist'),
		publicPath: '/',
		filename: '[name].js',
		chunkFilename: '[name].[chunkhash].js'
	},
	plugins: [
		// PLUGIN FOR CREATING VARIABLES ACCESSABLE IN ALL FILES
		// new webpack.ProvidePlugin({}),
		new CommonsPlugin({
			name: 'common',
			minChunks: Infinity 
		}),
		new HtmlWebpackPlugin({
			template: './src/index.html',
			inject: true
		})
	],
	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: [/node_modules/],
				loader: 'babel-loader',
				query: {
					presets: ['es2015']
				}
			},
			{
				test: /\.css$/,
				exclude: [/node_modules/],
				loader: 'style-loader!css-loader'
			}
		]
	},
	resolve: {
		extensions: ['', '.js']
	}
}

module.exports = config;