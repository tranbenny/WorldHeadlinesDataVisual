var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var reload = browserSync.reload;
var eslint = require('gulp-eslint');
var gutil = require('gulp-util');

var concat = require('gulp-concat'); // combines files into one
var uglify = require('gulp-uglify'); // minimizes file
var babelify = require('babelify'); // babel transpiler 
var es6 = require('babel-preset-es2015'); // es6 babel preset
var browserify = require('browserify'); // module builder
var watchify = require('watchify'); // watches for changes
var source = require('vinyl-source-stream'); // converts browserify stream to gulp stream

var config = {
	'js' : './client/js/**/*.js',
	'css' : './client/css/*.css',
	'index' : './client/index.html',
	'views' : './client/views/*.html',
	'main' : './client/js/app.js',
	'dist' : './client/src/*.json',
	'cssModules' : [
		'./node_modules/bootstrap/dist/css/bootstrap.min.css',
		'./node_modules/bootstrap/dist/css/bootstrap-theme.min.css',
		'./node_modules/ammap3/ammap/ammap.css'
	], 
	'jsModules' : [
		'./node_modules/jquery/jquery.min.js',
		'./node_modules/bootstrap/bootstrap.min.js',
		'./node_modules/ammap3/ammap/amma.js',
		'./node_modules/ammap3/ammap/maps/js/worldLow.js'
	]
};

function bundle(bundler) {
	return bundler
		.transform(babelify, {
			presets: [es6]
		})
		.bundle()
		.on('error', function(e) {
			gutil.log(e.message);
		})
		.pipe(source('bundle.js'))
		.pipe(gulp.dest('./dist/js'))
		.pipe(browserSync.stream());
}


// concatenate 3rd party css files
gulp.task('css-modules', function() {
	return gulp.src(config.cssModules)
		.pipe(concat('vendor.css'))
		.pipe(gulp.dest('dist/css'));
});

gulp.task('js-modules', function() {
	return gulp.src(config.jsModules)
		.pipe(concat('vendor.js'))
		.pipe(gulp.dest('dist/js'));
});


// browserSync.stream();


// code quality analysis
gulp.task('lint', function() {
	return gulp.src(config.js)
		.pipe(eslint());
});

// js build task
gulp.task('js', function() {
	return bundle(browserify(config.main));
});

// css build task
gulp.task('css', function() {
	return gulp.src(config.css)
		.pipe(concat('bundle.css'))
		.pipe(gulp.dest('dist/css'));
});

// views build task, copies views over to dist folder
gulp.task('views', function() {
	return gulp.src(config.views)
		.pipe(gulp.dest('dist/views'));
});

// copies index file to dist folder
gulp.task('copy-index', function() {
	return gulp.src(config.index)
		.pipe(gulp.dest('dist'));
});

gulp.task('copy-dist', function() {
	return gulp.src(config.dist)
		.pipe(gulp.dest('dist/src'));
});

gulp.task('watch', ['lint'], function() {
	var watcher = watchify(browserify(config.main), watchify.args);
	bundle(watcher);
	watcher.on('update', function() {
		bundle(watcher);
	});
	watcher.on('log', gutil.log);

	gulp.watch([config.index, config.views], ['views', 'copy-index']).on('change', reload);
	gulp.watch(config.js).on('change', reload);
	gulp.watch(config.css, ['css']).on('change', reload);

	browserSync.init({
		server: {
			baseDir: './dist',
			port: 5000
		}
	});
});


gulp.task('default', ['js-modules', 'css-modules', 'css', 'views','copy-index', 'lint', 'js', 'watch'])
