'use strict';

const path = require('path');
const MiniCssExtractPlugin = require(`mini-css-extract-plugin`);
const VueLoaderPlugin = require('vue-loader/lib/plugin');

const isDevelopmentMode = process.env.NODE_ENV !== 'production';

const config = {
    mode: 'production',
    entry: {
        global: './global/index.js',
        vendor: './vendor/index.js',

        component_demo: './components/demo-plugin/index.js',
    },
    output: {
        filename: '[name].js',
        path: __dirname + '/dist/',
        publicPath: '/static/dist/',
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
                use: [
                    {
                        loader: 'svg-url-loader',
                        options: {
                            encoding: 'base64',
                            iesafe: true,
                        },
                    },
                ],
            },
            {
                test: /\.(sass|scss|css)$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                    },
                    {loader: 'css-loader', options: {sourceMap: true}},
                    {
                        loader: 'postcss-loader',
                        options: {
                            postcssOptions: {
                                plugins: [['autoprefixer']],
                            },
                        },
                    },
                    {loader: 'sass-loader', options: {sourceMap: true}},
                ],
            },
            {
                // images
                test: /\.(jpe?g|png|gif)$/i,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            query: {
                                hash: 'sha512',
                                digest: 'hex',
                                name: '[name].[ext]',
                            },
                        },
                    },
                    {
                        loader: 'image-webpack-loader',
                        options: {
                            query: {
                                bypassOnDebug: 'true',
                                mozjpeg: {progressive: true},
                                gifsicle: {interlaced: true},
                                optipng: {optimizationLevel: 7},
                                webp: {quality: 80},
                            },
                        },
                    },
                ],
            },
            {
                test: /\.(svg)(\?[\s\S]+)?$/,
                // svg fonts cannot be processed the way we do with svg images above
                // therefore they are handled separately here
                include: /fonts/,
                use: ['file-loader'],
            },
            {
                test: /\.woff2?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'file-loader',
            },
            {
                test: /\.(ttf|eot)(\?[\s\S]+)?$/,
                loader: 'file-loader',
            },
            {
                test: /\.vue$/,
                use: [{loader: 'vue-loader'}],
            },
        ],
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js'],
        modules: [path.resolve('.'), 'node_modules'],
        alias: {
            vue:
                process.env.NODE_ENV === 'production' ?
                    'vue/dist/vue.min.js' : 'vue/dist/vue.js',
        },
    },
    devServer: {
        allowedHosts: [
            '.nip.io',
            '127.0.0.1',
            '0.0.0.0'
        ],
        hot: true, // HMR
        host: '0.0.0.0',
        port: 8090,
        headers: {
            'Access-Control-Allow-Origin': '*',
        }
    },
    plugins: [
        new VueLoaderPlugin(),
        new MiniCssExtractPlugin({filename: '[name].css'}),
    ],
};

if (isDevelopmentMode) {
    config.mode = 'development';
    config.devtool = 'eval-source-map';
    // those are twice as slow, but work with scss
    // config.devtool = 'source-map';
    config.output.filename = '[name].bundle.js';
    config.output.publicPath = 'http://localhost:8090/';
}

const isDockerMode = process.env.NODE_ENV === 'docker';
if (isDockerMode) {
    config.watchOptions = {
        poll: 100, // enable polling since fsevents are not supported in docker
    };
}

module.exports = config;
