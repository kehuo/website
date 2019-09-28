/*
 * @Author: Lucien Zhang
 * @Date:   2019-09-20 22:01:11
 * @Last Modified by:   Lucien Zhang
 * @Last Modified time: 2019-09-28 15:35:17
 */

// look into 127.0.0.1:3000!!! not 5000!!!

var gulp = require('gulp');
var browsersync = require("browser-sync").create();
var exec = require('child_process').exec;


gulp.task('runflask', function(done) {
    exec('python manage.py');
    done();
    console.log('Flask was launched');
});

gulp.task('build-server', function(done) {
    browsersync.init({
        proxy: "127.0.0.1:5000"
    });
    done();
    console.log('build-server proxy was launched');
});

gulp.task('browser-reload', function(done) {
    browsersync.reload();
    done();
    console.log('Browser reload completed');
});

gulp.task('watch-files', function(done) {
    gulp.watch("./app/templates/**/*.*", gulp.task('browser-reload'));
    gulp.watch("./app/static/**/*.*", gulp.task('browser-reload'));
    done();
    console.log(('gulp watch started'));
});

gulp.task('default', gulp.series('runflask', 'build-server', 'watch-files', function(done) {
    done();
    console.log('Default all task done!');
}));

