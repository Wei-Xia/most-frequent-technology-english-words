var gulp = require('gulp'),
	gulpLoadPlugins = require('gulp-load-plugins'),
	plugins = gulpLoadPlugins();

gulp.task('default', async function () {

	gulp.src('_layouts/dev.html')
		.pipe(plugins.cacheBust({
			type: 'MD5',
			basePath: './'
		}))
		.pipe(plugins.htmlmin({ collapseWhitespace: true }))
		.pipe(gulp.dest('_layouts'));

	gulp.src('assets/*.css')
		.pipe(plugins.cleanCss({ compatibility: 'ie8' }))
		.pipe(gulp.dest('build'));
});
