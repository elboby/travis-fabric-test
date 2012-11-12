from fabric.api import *

SERVERS = {}
SERVERS['aws'] = [
    'hero@ec2-54-247-135-204.eu-west-1.compute.amazonaws.com'
]
SERVERS['localbox'] = [
    'hero@192.168.3.201'
]
SERVERS['travis'] = [
    '127.0.0.1'
]


@task
def on_(machine):
    """ Setup machine environment """
    env.hosts = SERVERS[machine]

@task
def test():
    """ run simple test """
    local("pwd")
    run("pwd")