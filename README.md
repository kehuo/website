# website
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
![Repo size](https://img.shields.io/github/repo-size/LucienZhang/website)

This is a repository for my [personal website](http://47.92.105.114), using Flask framework.

The server is established from `manage.py` file in the root directory. The main application takes two blueprints from `website/blueprints` directory, one is a game engine for [The Werewolves of Millers Hollow]( https://en.wikipedia.org/wiki/The_Werewolves_of_Millers_Hollow), and another one is for showing some applications using machine learning or deep learning techniques.

Each blueprint can run on there own, please refer project [werewolf](https://github.com/LucienZhang/werewolf) or [ml](https://github.com/LucienZhang/ml) for details.

I deployed this website on a Ubuntu 16.04 server, with following structure:
<pre>
Nginx <==> gunicorn (serving flask) <==> MySQL
           gunicorn (serving flask) <==> Redis
</pre>

To deploy this website on your server, follow the next instructions:
1. clone this repository (since this project use other blueprints as submodules, you need clone this repository recursively)
2. create a virtual environment
3. install the requirements (since this website will use a blueprint for Machine Learning project, for GPU server, modify the file `requirements.txt`, change `-r website/blueprints/ml/cpu.requirements.txt` to `-r website/blueprints/ml/gpu.requirements.txt`, and then, run the following commands)
