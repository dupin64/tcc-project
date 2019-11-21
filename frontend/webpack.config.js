const BundleTracker = require("webpack-bundle-tracker");
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    context: __dirname,
    entry: {
        app: ["./src/main"]
    },

    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.(css|sass|scss)$/,
                use: ExtractTextPlugin.extract({
                    use: ['css-loader', 'sass-loader']
                })
            },
            {
                test: /\.(png|woff|woff2|eot|ttf|svg)$/,
                loader: 'url-loader?limit=100000'
            },
        ]
    },

    output: {
        path: require("path").resolve("../assets/bundles/"),
        filename: "app.js"
    },

    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: "webpack-stats.json"
        }),
        new VueLoaderPlugin(),
        new ExtractTextPlugin({filename: 'app.css', allChunks: true})
    ]
};
