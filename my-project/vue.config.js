const WorkerPlugin = require('worker-plugin')

module.exports = {
	publicPath: "./",
  // 输出文件目录
  	outputDir: "dist",
	assetsDir: 'static',
	lintOnSave: false,
	configureWebpack: {
		plugins:[
			new WorkerPlugin()
		]
	}
};