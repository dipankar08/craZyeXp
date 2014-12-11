module.exports = function(grunt) {

  // Project configuration.
  
  grunt.initConfig({


  //pkg: '<json:package.json>',

  sass: {
  options: {
    style: 'expanded'
          },
    dev: {
    files: [
     /*{
      expand: true,
      cwd: '../../static/scss/',
      src: '*.scss',
      dest: '../../static/scss/css/',
      ext: '.css'
    },*/
    {src: '../../static/scss/toothstrap.scss',dest: '../../static/scss/css/toothstrap.css'}
    ]
  }
  },//end of sass
cssbeautifier : {
  files : ["../../static/scss/css/*.css"],
  options : {
    indent: '  ',
    openbrace: 'end-of-line',
    autosemicolon: true
  }
},//end of cssbui

concat: {
  js: {
    src: '../../static/js/*.js',
    dest: '../../genApps/StaticFiles/js/concat.js'
  },
/*
  css: {
//    src: '../src/css/*.css',
    src: '../src/css/tootstrap.css',
    dest: '../dest/css/concat.css'
  }
},
*/
css: {
    src: '../../static/scss/css/*.css',
    dest: '../../genApps/StaticFiles/css/concat.css'
  }
}, //end of concat
  

'min': {
        'dist': {
                 'options': {
                 'report': 'gzip'
                            },
                 'files': [{
                    'src': '../../genApps/StaticFiles/js/concat.js',
                    'dest': '../../genApps/StaticFiles/js/concat.min.js'
                 }]
                        }
                },//endof min
'cssmin': {
            'dist': {
            'options': {
                  'report': false
            },
            'files': [{
                  'src': '../../genApps/StaticFiles/css/concat.css',
                  'dest': '../../genApps/StaticFiles/css/concat.min.css'
                   }]
                  }
                },//end of css min
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
    },//end of jshint

uglify: {}, //end of uglify

    watch: {
      css: {
        files: '../../static/**/*',
        tasks: ['sass','cssbeautifier','concat', 'min', 'cssmin','sync']
      }
    },//watches
    
sync: {
      main: {
        files: [{
          cwd: '../../static/html/',
          src: [
            '**', /* Include everything */
            '!**/*.txt' /* but exclude txt files */
          ],
          dest: '../../genApps/StaticFiles/html/',
        },
        { 
        cwd: '../../static/fonts/',
          src: [
            '**', /* Include everything */
            '!**/*.txt' /* but exclude txt files */
          ],
          dest: '../../genApps/StaticFiles/fonts/', 
        }
        ],
        //pretend: true, // Don't do any IO. Before you run the task with `updateAndDelete` PLEASE MAKE SURE it doesn't remove too much.
        verbose: true // Display log messages when copying files
      }
    },//end of sync

copy: {
  main: {
    files: [
      // includes files within path
      //{expand: true, src: ['path/*'], dest: 'dest/', filter: 'isFile'},

      // includes files within path and its sub-directories
      {expand: true, src: ['../../static/html/**'], dest: '../../genApps/StaticFiles/html/'},
      {expand: true, src: ['../../static/fonts/**'], dest: '../../genApps/StaticFiles/fonts/'},
      // makes all src relative to cwd
      //{expand: true, cwd: 'path/', src: ['**'], dest: 'dest/'},

      // flattens results to a single level
      //{expand: true, flatten: true, src: ['path/**'], dest: 'dest/', filter: 'isFile'},
    ],
  },
},

}); //end of config()

//grunt.loadTasks('tasks');
grunt.loadNpmTasks('grunt-contrib-sass');
grunt.loadNpmTasks('grunt-yui-compressor');
grunt.loadNpmTasks('grunt-contrib-concat');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-cssbeautifier');
grunt.loadNpmTasks('grunt-css');
grunt.loadNpmTasks('grunt-sync');
grunt.loadNpmTasks('grunt-contrib-copy');
// Default task.
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.registerTask('default',['watch']);  
//grunt.registerTask('default', ['sass','cssbeautifier','concat', 'min', 'cssmin','sync']);
};
