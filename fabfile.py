from os import getenv
from dotenv import load_dotenv
from fabric import Connection, task

load_dotenv()

SERVER_URL = getenv('SERVER_URL')
SERVER_USER = getenv('SERVER_USER')
SSH_PASSPHRASE = getenv('SSH_PASSPHRASE')

connect_kwargs = {
    'passphrase': SSH_PASSPHRASE
}

con = Connection(SERVER_URL, user=SERVER_USER, connect_kwargs=connect_kwargs, connect_timeout=0)


@task
def push(local, message):
    local.config['passphrase'] = SSH_PASSPHRASE
    local.run('git submodule foreach git pull', replace_env=False)
    local.run('git add website/blueprints/*', replace_env=False)
    local.run(f'git commit -m "{message}"', replace_env=False)
    local.run('git push', replace_env=False)


@task
def test(c, info):
    c.run('cd')
    c.run('git status', replace_env=False)
    # print(c)
    # local_ctx.run('git status')
    # result = c.run('git status')
    # print(result)
    # print(con.local('git status'))
    con.run('uname -s', timeout=None)
    print(info)
