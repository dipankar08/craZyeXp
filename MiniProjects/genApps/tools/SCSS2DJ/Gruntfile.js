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
      cwd: '../../static/css/',
      src: '*.scss',
      dest: '../../static/temp/css/',
      ext: '.css'
    },
    {src: '../../static/css/toothstrap.scss',dest: '../../genApps/StaticFiles/css/toothstrap.css'}
    ]
  }
  },//end of sass
cssbeautifier : {
  files : ["../../static/temp/css/*.css"],
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
    src: '../../static/temp/css/*.css',
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
        //tasks: ['sass']
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
        }],
        pretend: true, // Don't do any IO. Before you run the task with `updateAndDelete` PLEASE MAKE SURE it doesn't remove too much.
        verbose: true // Display log messages when copying files
      }
    }

}); //end of config()

//grunt.loadTasks('tasks');
grunt.loadNpmTasks('grunt-contrib-sass');
grunt.loadNpmTasks('grunt-yui-compressor');
grunt.loadNpmTasks('grunt-contrib-concat');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-cssbeautifier');
grunt.loadNpmTasks('grunt-css');
grunt.loadNpmTasks('grunt-sync');
// Default task.
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.registerTask('default',['watch']);  
//grunt.registerTask('default', ['sass','cssbeautifier','concat', 'min', 'cssmin','sync']);
};
