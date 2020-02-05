from os import getenv
from dotenv import load_dotenv
from fabric import Connection, task, Config

load_dotenv()

SERVER_URL = getenv('SERVER_URL')
SERVER_USER = getenv('SERVER_USER')
SSH_PASSPHRASE = getenv('SSH_PASSPHRASE')
SERVER_PATH = getenv('SERVER_PATH')
SERVER_NAME_PREFIX = getenv('SERVER_NAME_PREFIX')
SUDO_PASSWORD = getenv('SUDO_PASSWORD')

connect_kwargs = {
    'passphrase': SSH_PASSPHRASE
}

config = Config(overrides={'sudo': {'password': SUDO_PASSWORD}})
con = Connection(SERVER_URL, user=SERVER_USER, connect_kwargs=connect_kwargs, connect_timeout=0, config=config)


@task
def push(local, message):
    local.config['passphrase'] = SSH_PASSPHRASE
    local.run('git checkout dev', replace_env=False)
    local.run('git submodule foreach git pull', replace_env=False)
    local.run('git add website/blueprints/*', replace_env=False)
    local.run(f'git commit -m "{message}"', replace_env=False)
    local.run('git push', replace_env=False)


def get_server_name(env):
    return SERVER_NAME_PREFIX + '_' + env


def get_home_path(env):
    home_path = SERVER_PATH + '/' + get_server_name(env) + '/website'
    return home_path


@task
def update(local, env):
    # assert env in ['prod', 'dev', 'test']
    assert env in ['prod', 'dev']
    with con.cd(SERVER_PATH + '/'):
        # con.run('ls')
        with con.cd(get_server_name(env) + '/website'):
            # con.run('pwd')
            # con.run('git status')
            # con.run('sudo supervisorctl status')
            # con.sudo('pwd')
            con.run('git pull')
            con.run('git submodule update')
            # con.sudo(f'supervisorctl restart {get_server_name(env)}')
    # because of STUPID Fabric 2!!
    # con.sudo(f'bash -c "cd {get_home_path(env)} && supervisorctl status {get_server_name(env)}"')
    con.sudo(f'bash -c "cd {get_home_path(env)} && supervisorctl restart {get_server_name(env)}"')


@task
def h5(local, env):
    assert env in ['prod', 'dev', 'test']


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
