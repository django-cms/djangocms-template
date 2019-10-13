'use strict';


const path = require('path');
const MiniCssExtractPlugin = require(`mini-css-extract-plugin`);


const isServerMode = process.env.NODE_ENV === 'production';


const config = {
    entry: {
        global: './frontend/global/index.js',

        homepage: './frontend/pages/homepage/index.js',
    },
    output: {
        filename: '[name].bundle.js',
        path: __dirname + '/dist/',
        publicPath: `http://localhost:8090/assets/`,
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
                test: /\.(sass|scss|css)$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader,
                        options: {
                            sourceMap: true,
                            plugins: () => {
                                return [
                                    require('precss'),
                                    require('autoprefixer'),
                                ];
                            },
                            hmr: true,
                        }
                    },
                    {loader: 'css-loader', options: {sourceMap: true}},
                    {loader: 'sass-loader', options: {sourceMap: true}},
                ]
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
                                name: '[name].[ext]'
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
                use: ['file-loader'],
            },
            {
                test: /\.(ttf|eot)(\?[\s\S]+)?$/,
                include: /fonts/,
                use: ['file-loader'],
            },
            {
                test: /\.modernizrrc.js$/,
                use: ['modernizr-loader'],
            },
            {
                test: /\.modernizrrc(\.json)?$/,
                use: ['modernizr-loader', 'json-loader'],
            }
        ],
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js',],
        modules: [
            path.resolve('frontend'),
            'node_modules'
        ],
        alias: {
            modernizr$: path.resolve(__dirname, '/frontend/.modernizrrc'),
        }
    },
    devServer: {
        contentBase: path.resolve(__dirname, `frontend`),
        headers: {'Access-Control-Allow-Origin': '*'},
        host: `localhost`,
        port: 8090,
        hot: true,
        inline: true,
    },
    plugins: [
        new MiniCssExtractPlugin({filename: '[name].css'}),
    ],
    devtool: 'cheap-module-source-map',
    optimization: {
        // the default config from webpack docs
        splitChunks: {
            chunks: 'async',
            minSize: 30000,
            maxSize: 0,
            minChunks: 1,
            maxAsyncRequests: 5,
            maxInitialRequests: 3,
            automaticNameDelimiter: '~',
            name: true,
            cacheGroups: {
                vendors: {
                    test: /[\\/]node_modules[\\/]/,
                    priority: -10,
                },
                default: {
                    minChunks: 2,
                    priority: -20,
                    reuseExistingChunk: true,
                },
            },
        },
    },
};


if (isServerMode) {
    config.mode = 'production';
    config.devtool = 'none';
    config.output.filename = '[name].js';
    config.output.publicPath = '/frontend/dist/';
}


module.exports = config;
