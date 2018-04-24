var gulp = require('gulp'),
  gulpLoadPlugins = require('gulp-load-plugins'),
  plugins = gulpLoadPlugins();

var cdnUrl = [
	[ 'assets/vue.js', 'https://anw.red/js/vue.min.js' ],
	[ 'assets/', 'https://anw.red/anyway.abc/' ]
];

gulp.task('default', function() {

	gulp.src('_layouts/dev.html')
		.pipe(plugins.cacheBust({
      type: 'MD5',
      basePath: './'
    	}))
		.pipe(plugins.batchReplace(cdnUrl))
    .pipe(plugins.htmlmin({collapseWhitespace: true}))
    .pipe(plugins.rename("production.html"))
		.pipe(gulp.dest('_layouts'));

	gulp.src('assets/*.css')
  	.pipe(plugins.cleanCss({compatibility: 'ie8'}))
    .pipe(plugins.batchReplace(cdnUrl))
    .pipe(gulp.dest('builds'));
});
