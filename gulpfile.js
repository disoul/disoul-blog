var gulp = require('gulp'),
    compass = require('gulp-compass'),
	path = require('path');

gulp.task('compass',function(){
	gulp.src('./blog/static/sass/index.scss')
	.pipe(compass({
		project: path.join(__dirname,'./blog/static'),
		css: 'css',
		sass: 'sass',
		image: 'image'
	}));
	gulp.src('./blog/static/sass/article.scss')
	.pipe(compass({
		project: path.join(__dirname,'./blog/static'),
		css: 'css',
		sass: 'sass',
		image: 'image'
	}));
	gulp.src('./blog/static/sass/aboutme.scss')
	.pipe(compass({
		project: path.join(__dirname,'./blog/static'),
		css: 'css',
		sass: 'sass',
		image: 'image'
	}));
	gulp.src('./blog/static/sass/tag.scss')
	.pipe(compass({
		project: path.join(__dirname,'./blog/static'),
		css: 'css',
		sass: 'sass',
		image: 'image'
	}));
});

gulp.task('sass:watch',function(){
	gulp.watch('./blog/static/sass/**/*.scss',['compass']);
});

gulp.task('default', function() {
  // place code for your default task here
});

