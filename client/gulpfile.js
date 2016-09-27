var gulp = require('gulp');
var gutil = require('gulp-util');
var shell = require('gulp-shell');
var webpack = require('webpack-stream');

var webpackConfig = require('./webpack.config.js');

var browserSync = require('browser-sync');
var reload = browserSync.reload;

gulp.task('server', ['webpack:build-dev', 'html-templates'], function() {
	browserSync.init({
		server: {
			baseDir: './dist'
		},
		port: 9000
	});
});

gulp.task('webpack:build-dev', ['js-lint'], function() {
	// TODO: INSERT PATH HERE
	return gulp.src(['./src/app.js'])
		.pipe(webpack(webpackConfig, null, function(err, stats) {
			if (err) throw new gutil.PluginError('webpack', err);
		}))
		.on('error', function(error) {
			gutil.log(error.message)
			this.emit('end');
		})
		.pipe(gulp.dest('dist/'));
});

gulp.task('watch-changes', function() {
	gulp.watch(["src/**/*"], ['reload-changes']);
});

gulp.task('reload-changes', ['webpack:build-dev'], function() {
	reload();
});

gulp.task('js-lint', function() {
	// TODO: SET UP CODE LINTING
});

// COPY ALL OTHER TEMPLATES 
gulp.task('html-templates', function() {
	return gulp.src(['./src/index.html'])
		.pipe(gulp.dest('dist/'));
});

gulp.task('test', shell.task([
	'karma start'
]));


gulp.task('default', ['server', 'watch-changes']);