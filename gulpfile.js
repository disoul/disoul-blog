var gulp = require('gulp'),
    compass = require('gulp-compass'),
	path = require('path');

gulp.task('compass',function(){
	gulp.src([
        './blog/static/sass/index.scss', './blog/static/sass/article.scss',
        './blog/static/sass/aboutme.scss', './blog/static/sass/tag.scss',
        './blog/static/sass/404.scss'
    ])
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

