module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
//pkg: '<json:package.json>',

sass: {
  options: {
    style: 'expanded'
  },
  dev: {
    files: [{
      expand: true,
      cwd: '../src/css/',
      src: '*.scss',
      dest: '../src/css/',
      ext: '.css'
    }]
  }
},
cssbeautifier : {
  files : ["../src/**/*.css"],
  options : {
    indent: '  ',
    openbrace: 'end-of-line',
    autosemicolon: true
  }
},

concat: {
  js: {
    src: '../src/js/*.js',
    dest: '../dest/js/concat.js'
  },
  css: {
    src: '../src/css/*.css',
    dest: '../dest/css/concat.css'
  }
},

/*    
min: {
  dist: {
    src: '../dest/js/concat.js',
    dest: '../dest/js/concat.min.js'
  }
},
cssmin: {
  dist:{
    src: '../dest/css/concat.css',
    dest: '../dest/css/concat.min.css'
  }
},
*/
'min': {
        'dist': {
                 'options': {
                 'report': 'gzip'
                            },
                 'files': [{
                    'src': '../dest/js/concat.js',
                    'dest': '../dest/js/concat.min.js'
                 }]
                        }
                },
'cssmin': {
            'dist': {
            'options': {
                  'report': false
            },
            'files': [{
                  'src': '../dest/css/concat.css',
                  'dest': '../dest/css/concat.min.css'
                   }]
                  }
                },
jshint: {
      options: {
        curly: true,
        eqeqeq: true,
        immed: true,
        latedef: true,
        newcap: true,
        noarg: true,
        sub: true,
        undef: true,
        boss: true,
        eqnull: true,
        node: true
      },
      globals: {
        exports: true,
        module: false
      }
    },

uglify: {}
  }
);
//grunt.loadTasks('tasks');
grunt.loadNpmTasks('grunt-contrib-sass');
grunt.loadNpmTasks('grunt-yui-compressor');
grunt.loadNpmTasks('grunt-contrib-concat');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-cssbeautifier');
grunt.loadNpmTasks('grunt-css');
  // Default task.
 grunt.registerTask('default', ['sass','cssbeautifier','concat', 'min', 'cssmin']);

};
