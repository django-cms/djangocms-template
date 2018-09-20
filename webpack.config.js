'use strict';
process.traceDeprecation = true;
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const path = require("path");
require('webpack');


let config = {
    mode: "development",
    entry: {
        app: ["./private/main.js"]
    },
    output: {
        path: __dirname + '/static/dist/', // `dist` is the destination
        publicPath: process.env.DEV_SERVER_PUBLIC_PATH,
        filename: "bundle.js",
        // chunkFilename: '[name].bundle.js',
    },
    // optimization: {
    // only useful if there are multiple entries, see https://webpack.js.org/guides/code-splitting/
    // this would require dynamic asset loading
    //     splitChunks: {
    //         chunks: 'all'
    //     }
    // },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.js$/, //Check for all js files
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                }
            },
            // svg needs to be loaded separately
            {
                test: /\.svg$/i,
                // fonts need to be loaded
                exclude: /fonts/,
                loader: "svg-url-loader",
            },
            {
                test: /\.(sass|scss|css)$/, //Check for sass or scss file names
                use: [{
                    loader: 'style-loader', // inject CSS to page
                }, {
                    loader: 'css-loader', options: {
                        sourceMap: true
                    }// translates CSS into CommonJS modules
                }, {
                    loader: 'postcss-loader', // Run post css actions
                    options: {
                        plugins: function () { // post css plugins, can be exported to postcss.config.js
                            return [
                                require('precss'),
                                require('autoprefixer')
                            ];
                        }
                    }
                }, {
                    loader: 'sass-loader', options: {
                        sourceMap: true
                    } // compiles Sass to CSS

                }]
            },
            // images
            {
                test: /\.(jpe?g|png|gif)$/i,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            query: {
                                hash: "sha512",
                                digest: "hex",
                                name: "[name]-[hash].[ext]"
                            }
                        }
                    },
                    {
                        loader: "image-webpack-loader",
                        options: {
                            query: {
                                bypassOnDebug: "true",
                                mozjpeg: {
                                    progressive: true
                                },
                                gifsicle: {
                                    interlaced: true
                                },
                                optipng: {
                                    optimizationLevel: 7
                                }
                            }
                        }
                    }
                ]
            },
            {
                test: /\.json$/,
                loader: "json-loader"  //JSON loader
            },
            {
                test: /\.(woff2?|ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                use: [
                    "file-loader"
                ]
            },
            {
                test: /\.(svg)(\?[\s\S]+)?$/,
                include: /fonts/,
                use: [
                    'file-loader'
                ]
            },
            {
                test: /\.modernizrrc$/,
                use: [
                    'modernizr-loader',
                    'json-loader'
                ]
            }
        ]
    },
    plugins: [
        new BrowserSyncPlugin({
            // browse to http://localhost:3000/ during development,
            // ./public directory is being served
            host: 'localhost',
            port: 3000,
            open: false,
            // server: { baseDir: __dirname },
            proxy: 'http://localhost:8090/'
        })
    ],
    //To run development server
    devServer: {
        contentBase: __dirname + '/private',
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
            "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
        }
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js'],
        alias: {
            modernizr$: path.resolve(__dirname, "./private/.modernizrrc"),
            // https://github.com/Eonasdan/bootstrap-datetimepicker/issues/1662
            jquery: path.join(__dirname, 'node_modules/jquery/dist/jquery')
        }
    },
    devtool: "eval-source-map" // Default development sourcemap
};

// Check if build is running in production mode, then change the sourcemap type
if (process.env.NODE_ENV === "production") {
    config.mode = "production";
    config.devtool = "source-map";
    config.context = __dirname + '/private';
    config.entry = {
        app: './main.js'
    };
    config.output = {
        path: __dirname + '/static/dist/', // `dist` is the destination
        filename: '[name].js',
        publicPath: "/static/dist/",
    };

    // Can do more here
    // JSUglify plugin
    // Offline plugin
    // Bundle styles seperatly using plugins etc,
}

module.exports = config;
