# website
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
![Repo size](https://img.shields.io/github/repo-size/LucienZhang/website)

This is a repository for my [personal website](http://47.92.105.114), using Flask framework.

The server is established from `manage.py` file in the root directory. The main application takes two blueprints from `website/blueprints` directory, one is a game engine for [The Werewolves of Millers Hollow]( https://en.wikipedia.org/wiki/The_Werewolves_of_Millers_Hollow), and another one is for showing some applications using machine learning or deep learning techniques.

Each blueprint can run on there own, please refer project [werewolf](https://github.com/LucienZhang/werewolf) or [ml](https://github.com/LucienZhang/ml) for details.

I deployed this website on a Ubuntu 18.04 server, with following structure:
<pre>
Nginx <==> gunicorn (serving flask) <==> MySQL
           gunicorn (serving flask) <==> Redis
</pre>

To deploy this website on your server, follow the next instructions:

1. Clone this repository.

   > Since this project is using other blueprints as submodules, you need to clone this repository recursively.

   ```bash
   $ sudo mkdir -p /var/www/[your domain name]
   $ cd /var/www/[your domain name]
   $ git clone --recursive https://github.com/LucienZhang/website.git
   ```

2. Install Miniconda and create a virtual environment, please refer to [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for details.

   ``````bash
   $ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   $ ./Miniconda3-latest-Linux-x86_64.sh
   # Install
   # You may need to modify the authorization for some files to enable creating a new environment by non-root user
   $ conda create -n website python=3.7
   $ conda activate website
   $ cd website
   $ pwd
   /var/www/[your domain name]/website
   ``````

3. Install the requirements 

   > Since this project is using a blueprint for Machine Learning project, for GPU server, modify the file `requirements.txt`, change `-r website/blueprints/ml/cpu.requirements.txt` to `-r website/blueprints/ml/gpu.requirements.txt`.

   ```bash
   $ pwd
   /var/www/[your domain name]/website
   $ conda env list
   # conda environments:
   #
   base                     /home/username/miniconda3
   website               *  /home/username/miniconda3/envs/website
   $ sudo apt install libmysqlclient-dev
   $ pip install -r requirements.txt
   ```

4. Install and configure Redis server, please refer [Redis](https://redis.io/topics/quickstart) for details

   ```bash
   $ cd /tmp
   $ wget http://download.redis.io/redis-stable.tar.gz
   $ tar xvzf redis-stable.tar.gz
   $ cd redis-stable
   $ make
   $ make test
   $ sudo make install
   $ sudo mkdir /etc/redis
   $ sudo cp /tmp/redis-stable/redis.conf /etc/redis/
   $ sudo vim /etc/redis/redis.conf
   ```

   > In the file `redis.conf`, set `supervised` from **`no`** to **`systemd`**, and set `dir` to **`/var/lib/redis`**

   ```bash
   ...
   supervised systemd
   ...
   ...
   dir /var/lib/redis
   ...
   ```

   ```bash
   $ sudo vim /etc/systemd/system/redis.service
   
   [Unit]
   Description=Redis In-Memory Data Store
   After=network.target
   
   [Service]
   User=redis
   Group=redis
   ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf
   ExecStop=/usr/local/bin/redis-cli shutdown
   Restart=always
   
   [Install]
   WantedBy=multi-user.target
   
   $ sudo adduser --system --group --no-create-home redis
   $ sudo mkdir /var/lib/redis
   $ sudo chown redis:redis /var/lib/redis
   $ sudo chmod 770 /var/lib/redis
   $ sudo systemctl start redis
   $ sudo systemctl status redis
   $ redis-cli
   127.0.0.1:6379> ping
   PONG
   127.0.0.1:6379> set test "It's working!"
   OK
   127.0.0.1:6379> get test
   "It's working!"
   127.0.0.1:6379> exit
   $ sudo systemctl restart redis
   $ redis-cli
   127.0.0.1:6379> get test
   "It's working!"
   127.0.0.1:6379> exit
   sudo systemctl enable redis
   Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /etc/systemd/system/redis.service.
   ```

5. Install and configure MySQL

   ```bash
   $ sudo apt-get update
   $ sudo apt-get install mysql-server
   $ mysql --version
   $ sudo mysql -u root -p
   Enter password: [your password for root user in MySQL]
   ```

   ```mysql
   mysql> CREATE USER 'mysql_user'@'%' IDENTIFIED BY 'mysql_password';
   mysql> CREATE DATABASE `database_name` CHARACTER SET utf8 COLLATE utf8_general_ci;
   mysql> GRANT ALL PRIVILEGES ON *.* TO 'mysql_user'@'%';  #No, dont do this, its a joke
   mysql> GRANT SELECT, INSERT, UPDATE, DELETE ON database_name.* TO 'mysql_user'@'localhost' IDENTIFIED BY 'mysql_password';
   mysql> FLUSH PRIVILEGES;
   mysql> SHOW GRANTS FOR 'mysql_user'@'localhost';
   ```

6. Configure project

   ```bash
   $ cd /var/www/[your domain name]/website/website
   $ mkdir instance
   $ cd instance
   $ sudo vim config.py
   
   from urllib.parse import quote
   
   DEBUG = False
   SECRET_KEY = 'secret key used for connecting mysql'
   SQLALCHEMY_DATABASE_URI = "mysql://mysql_user:%s@localhost:3306/database_name?charset=utf8" % quote('mysql_password')
   SQLALCHEMY_ECHO = True
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   LOGIN_SECRET_KEY = 'secret key used for flask login'
   REDIS_URL = "redis://localhost"
   ```

   run script to load h5 file?

   wget -q http://www.whatever.com/filename.txt -O /path/filename.txt 

7. Install and setup supervisor

8. Install and setup nginx

9. 