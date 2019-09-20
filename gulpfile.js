/*
* @Author: Lucien Zhang
* @Date:   2019-09-20 22:01:11
* @Last Modified by:   Lucien Zhang
* @Last Modified time: 2019-09-20 22:58:04
*/

// look into 127.0.0.1:3000!!! not 5000!!!

var gulp = require('gulp');
var browsersync = require("browser-sync").create();
var exec = require('child_process').exec;


gulp.task('runflask', function (done) {
    exec('python app.py');
    done();
    console.log('Flask was launched');
});

gulp.task('build-server', function (done) {
    browsersync.init({
        proxy: "127.0.0.1:5000"
    });
    done();
    console.log('build-server proxy was launched');
});

gulp.task('browser-reload', function (done){
    browsersync.reload();
    done();
    console.log('Browser reload completed');
});

gulp.task('watch-files', function(done) {
    gulp.watch("./templates/**/*.*", gulp.task('browser-reload'));
    gulp.watch("./static/**/*.*", gulp.task('browser-reload'));
    done();
    console.log(('gulp watch started'));
});

gulp.task('default', gulp.series('runflask', 'build-server', 'watch-files', function(done){
    done();
    console.log('Default all task done!');
}));


























// /*
// * @Author: Lucien Zhang
// * @Date:   2019-09-16 21:46:27
// * @Last Modified by:   Lucien Zhang
// * @Last Modified time: 2019-09-20 18:42:20
// */
// var gulp = require('gulp');
// var browserSync = require('browser-sync').create();
// // var reload = browserSync.reload;
// var exec = require('child_process').exec;

// // // Static server
// // gulp.task('browser-sync', function() {
// //     browserSync({
// //         server: {
// //             //指定服务器启动根目录
// //             baseDir: "."
// //         }
// //     });
// //     //监听任何文件变化，实时刷新页面
// //     gulp.watch("./**/*.*").on('change', browserSync.reload);
// // });


// //Run Flask Server
// gulp.task('browser-sync', function() {
//     browserSync.init({
//         open: false,
//         files: ['templates/**/*.*','static/**/*.*'],
//         proxy: "127.0.0.1:5000"
//     });
// });

// gulp.task('reload', function(done) {
//   browserSync.reload();
//   done();
// });

// // gulp.task('watch:dist', function() {
// //   return gulp.watch('./dist/**/*',
// //   gulp.series('reload'));
// // });



// // var config = {
// //     paths: {
// //         css: './src/css/**/*'
// //     }
// // };

// // gulp.task('watch:css', function() {
// //     return gulp.watch(config.paths.css,
// //         gulp.series('css:dev'));
// // });

// gulp.task('watch', function(){
//     return gulp.watch(['templates/**/*.*','static/**/*.*'], gulp.series('reload'));
// });

// gulp.task('default',gulp.parallel('watch','browser-sync'));

// // function runflask(){
// //     exec('python app.py');
// // }

// // function browsersync(){
// //     browserSync.init({
// //         open: false,
// //         //injectChanges: true,
// //         proxy: "127.0.0.1:5000"
// //         //notify: false
// //     });
// // }

// // function watch() {
// //     //gulp.watch(['templates/**/*.*','static/**/*.*']);
// //     gulp.watch(['templates/**/*.*','static/**/*.*'], reload);//.on('change', reload);
// // }

// // function reload(done){
// //     browserSync.reload();
// //     done();
// // }

// // gulp.task('runflask', runflask);

// // gulp.task('browser-sync', browsersync);

// // // gulp.task('browser-sync',gulp.series('runflask',function(){
// // //     browserSync.init({
// // //         proxy: "127.0.0.1:5000",
// // //         //files: ['templates/**/*.*','static/**/*.*'],
// // //         notify: false
// // //     });
// // //     // var bs = browserSync.create();
// // //     // bs.watch(['templates/**/*.*','static/**/*.*']).on('change', bs.reload);
// // //     // bs.init({
// // //     //     proxy: "127.0.0.1:5000"
// // //     // });


// // //   // browserSync({
// // //   //   // notify: false,
// // //   //   proxy: "127.0.0.1:5000"
// // //   // });
// // //   // done();
// // // }));


// // gulp.task('watch', watch);

// // // gulp.task('default', gulp.parallel('watch','browser-sync'));

// // // gulp.task('bs',gulp.series('runflask',function(){
// // //     exec('browser-sync start --proxy http://127.0.0.1:5000/ --files="templates/**, static/**"');
// // // }));





// // // gulp.task('default',gulp.parallel('runflask',function(){
// // //     browserSync.init({
// // //         proxy: "127.0.0.1:5000",
// // //         //files: ['templates/**/*.*','static/**/*.*'],
// // //         notify: false
// // //     });

// // //     gulp.watch(['templates/**/*.*','static/**/*.*'],browserSync.reload());//.on('change', browserSync.reload);

// // // }));



// // gulp.task('default', gulp.parallel(runflask,browsersync,watch));
