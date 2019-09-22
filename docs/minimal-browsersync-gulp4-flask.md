# Minimal BrowserSync + Gulp 4 + Flask Setup

This configuration is not limited to flask, it is actually a combination of **browser-sync + gulp 4 + any other server**, our target is to browser-sync as a proxy, and finally to have the browser updated **AUTOMATICALLY**!!

Before you read this document, if you tried so many ways for this combination and didn't work, you may have been debugging the wrong port. Use port 3000(port of browser-sync) NOT 5000(port of flask)!!


## Step 1: Install node.js and npm

<https://nodejs.org/en/download/current/>

Select a correct version, download and install it

After installation, check node.js and npm are available

```bash
node --version
npm --version
```

## Step 2: Install gulp

```bash
npm install --global gulp-cli

mkdirp my-project
cd my-project
npm init

npm install --save-dev gulp
```

If you check your gulp version in `my-project`,there will be two gulp versions!

```bash
$ gulp --version

CLI version: 2.2.0
Local version: 4.0.2
```

## Step 3: Install browser-sync

```bash
npm install browser-sync --save-dev
```

## Step 4: Write the gulpfile.js

create a file named `gulpfile.js` under `my-project` folder

```bash
touch gulpfile.js
```

Then write it!

```javascript
var gulp = require('gulp');
var browsersync = require("browser-sync").create();
var exec = require('child_process').exec;


gulp.task('runflask', function(done) {
    exec('python app.py');
    done();
    console.log('Flask was launched');
});

gulp.task('build-server', function(done) {
    browsersync.init({
        proxy: "127.0.0.1:5000"  //flask should also run in 5000 port
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
    gulp.watch("./templates/**/*.*", gulp.task('browser-reload'));
    gulp.watch("./static/**/*.*", gulp.task('browser-reload'));
    done();
    console.log(('gulp watch started'));
});

gulp.task('default', gulp.series('runflask', 'build-server', 'watch-files', function(done) {
    done();
    console.log('Default all task done!');
}));

```

There are too many problems with gulp 4, but finally, the above configuration works!

## Step 5: File Structure & app.py

The file structure is like this:

```
my-project
│   gulpfile.js
│   app.py
|
└───templates
│   │   index.html
|    
└───static
    │   css
    │   js
```


This is how `app.py` looks like:
```python3
# app.py
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def homepage():
    return render_template("index.html")

# this is very important!! to disable cache when you develop it
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

if __name__ == '__main__':
    # app.run(debug=True, port=5000)
    app.run() # port=5000 as default
```

## Setp 6: Run

Under `my-project` folder, run gulp
```
$ gulp
[21:22:10] Using gulpfile D:\Projects\my-project\gulpfile.js
[21:22:10] Starting 'default'...
[21:22:10] Starting 'runflask'...
[21:22:10] Finished 'runflask' after 9.17 ms
[21:22:10] Starting 'build-server'...
Flask was launched
[21:22:10] Finished 'build-server' after 20 ms
[21:22:10] Starting 'watch-files'...
build-server proxy was launched
[21:22:10] Finished 'watch-files' after 26 ms
[21:22:10] Starting '<anonymous>'...
gulp watch started
[21:22:10] Finished '<anonymous>' after 2.32 ms
[21:22:10] Finished 'default' after 68 ms
Default all task done!
[Browsersync] Proxying: http://127.0.0.1:5000
[Browsersync] Access URLs:
 ------------------------------------
       Local: http://localhost:3000
    External: http://192.168.3.3:3000
 ------------------------------------
          UI: http://localhost:3001
 UI External: http://localhost:3001
 ------------------------------------
```

## FINAL STEP
**to debug your project in `http://localhost:3000` port 3000!!! NOT 5000!!!**
flask server needs time to start up, so wait that page for a while or press F5 to load it (just once), then you can see `Browsersync: connected` at the top right conor of your browser. the page will be updated **automatically** when you change files in templates or static

