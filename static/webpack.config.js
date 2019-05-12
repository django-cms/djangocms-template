'use strict';

const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');


const config = {
    entry: {
        global: './static/global/index.js',
        // pages
        homepage: './static/pages/homepage/index.js',
    },
    output: {
        filename: '[name].bundle.js',
        path: __dirname + '/dist/',
        publicPath: process.env.DEV_SERVER_PUBLIC_PATH,
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.svg$/i,
                exclude: /fonts/,
                loader: 'svg-url-loader',
            },
            {
                test: /\.(sass|scss)$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader',
                ]
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            // images
            {
                test: /\.(jpe?g|png|gif)$/i,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            query: {
                                hash: 'sha512',
                                digest: 'hex',
                                name: '[name]-[hash].[ext]'
                            }
                        }
                    },
                    {
                        loader: 'image-webpack-loader',
                        options: {
                            query: {
                                bypassOnDebug: 'true',
                                mozjpeg: {progressive: true},
                                gifsicle: {interlaced: true},
                                optipng: {optimizationLevel: 7},
                            }
                        }
                    }
                ]
            },
            {
                test: /\.woff2?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: ['file-loader']
            },
            {
                test: /\.(ttf|eot|svg)(\?[\s\S]+)?$/,
                include: /fonts/,
                use: ['file-loader']
            },
            {
                test: /\.modernizrrc$/,
                use: ['modernizr-loader', 'json-loader']
            },
        ],
    },
    resolve: {
        extensions: [ '.ts', '.tsx', '.js' ]
    }
    // plugins: [
    //     new BundleTracker({
    //         path: __dirname,
    //         filename: './webpack-stats.json'
    //     }),
    //     new UglifyJsPlugin(),
    // ],
    // //To run development server
    // devServer: {
    //     contentBase: '/static',
    //     headers: {
    //         'Access-Control-Allow-Origin': '*',
    //         'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
    //         'Access-Control-Allow-Headers': 'X-Requested-With, content-type, Authorization'
    //     }
    // },
    // resolve: {
    //     extensions: ['.tsx', '.ts', '.js'],
    //     alias: {
    //         modernizr$: path.resolve(__dirname, './private/.modernizrrc'),
    //         // https://github.com/Eonasdan/bootstrap-datetimepicker/issues/1662
    //         jquery: path.join(__dirname, 'node_modules/jquery/dist/jquery')
    //     }
    // },
    // devtool: 'eval-source-map' // Default development sourcemap
};

// Check if build is running in production mode, then change the sourcemap type
// if (process.env.NODE_ENV === 'production') {
//     config.devtool = 'source-map';
//     config.context = __dirname + '/static';
//     config.entry = {
//         app: './static/ts/index.js'
//     };
//     config.output = {
//         path: __dirname + '/static/dist/',
//         filename: '[name]-[chunkhash].js',
//         publicPath: '/static/dist/',
//     };
// }

module.exports = config;
