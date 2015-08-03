/*global module:false*/
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    meta: {
	  scssPath: './blog/static/css/scss/',
	  cssPath: './blog/static/css/'
	},

    banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' +
      '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
      '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
      '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
      ' Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %> */\n',
    // Task configuration.
    // Bower
    bower: {
      install: {
		options: {
		  "targetDir": "./blog/static/lib",
          "layout": "byType",
          "install": true,
          "verbose": false,
          "cleanTargetDir": false
		}
      }
    },

	// Sass
    sass:{
	  dist:{
	    options:{
		  style: "compressed",
		},
		files: {
		  '<%= meta.cssPath %>index.css': '<%= meta.scssPath %>index.scss',
		  '<%= meta.cssPath %>tag.css': '<%= meta.scssPath %>tag.scss',
		  '<%= meta.cssPath %>aboutme.css': '<%= meta.scssPath %>aboutme.scss',
		  '<%= meta.cssPath %>article.css': '<%= meta.scssPath %>article.scss',
		  '<%= meta.cssPath %>404.css': '<%= meta.scssPath %>404.scss',
		}
	  }
	},

	// Watch
    watch: {
	  script: {
		files: [
		  '<%= meta.scssPath%>/**/*.scss'
		],
		tasks: ['sass'],
		options: {
		},
	  }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-bower-task');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task.
  grunt.registerTask('default', ['sass']);

};
