/*
* @Author: Lucien Zhang
* @Date:   2019-09-16 21:46:27
* @Last Modified by:   Lucien Zhang
* @Last Modified time: 2019-09-16 21:48:33
*/
var gulp = require('gulp');
var browserSync = require('browser-sync');
// Static server
gulp.task('browser-sync', function() {
    browserSync({
        server: {
            //指定服务器启动根目录
            baseDir: "."
        }
    });
    //监听任何文件变化，实时刷新页面
    gulp.watch("./**/*.*").on('change', browserSync.reload);
});
