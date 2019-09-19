/*
* @Author: Lucien Zhang
* @Date:   2019-09-16 21:46:27
* @Last Modified by:   Lucien Zhang
* @Last Modified time: 2019-09-19 17:31:29
*/
var gulp = require('gulp');
var browserSync = require('browser-sync');
var exec = require('child_process').exec;

// // Static server
// gulp.task('browser-sync', function() {
//     browserSync({
//         server: {
//             //指定服务器启动根目录
//             baseDir: "."
//         }
//     });
//     //监听任何文件变化，实时刷新页面
//     gulp.watch("./**/*.*").on('change', browserSync.reload);
// });

gulp.task('runflask',done=>{
    var proc=exec('python app.py');
    done();
});

gulp.task('default',gulp.series('runflask',done=>{
    browserSync({
    notify: false,
    proxy: "127.0.0.1:5003"
  });

    gulp.watch(['templates/**/*.*','static/**/*.*']).on('change', browserSync.reload);

    done();
}));
