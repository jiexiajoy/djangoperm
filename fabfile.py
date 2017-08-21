#! -*- coding: utf-8 -*-

from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import confirm


# build-in
env.hosts = [
    'root@10.2.5.51:22',
    'root@123.59.27.192:22'
]
env.passwords = {
    'root@10.2.5.51:22': 'PyFansLi050318',
}
env.key_filename = [None, '~/.ssh/root@123.59.27.192:22.pem']

# customer
env.git_ssh = 'git@github.com:xmdevops/djangoperm.git'
env.remote_dir = '/xm-workspace/xm-apps/djangoperm/'



def test():
    print green('test success.')


def add():
    with settings(warn_only=True):
        result = local('git add -A', capture=True)
        if result.failed and not confirm('git add failed, continue anyway? '):
            abort(red('aborting with user request - git add'))
    print green('git add success.')


def commit():
    with settings(warn_only=True):
        message = prompt('commit message: ', default='djangoperm')
        result = local('git commit -m "{0}"'.format(message), capture=True)
        if result.failed and not confirm('git commit failed, continue anyway? '):
            abort(red('aborting with user request - git commit'))
    print green('git commit success.')


def push():
    with settings(warn_only=True):
        result = local('git push', capture=True)
        if result.failed and not confirm('git push failed, continue anyway? '):
            abort(red('aborting with user request - git push'))
    print green('git push success.')


def prepare_deploy():
    test()
    add()
    commit()
    push()


def deploy():
    with settings(warn_only=True):
        result = run('test -d {0}'.format(env.remote_dir))
        if result.failed:
            run('git clone {0} {1}'.format(env.git_ssh, env.remote_dir))
    with cd(env.remote_dir):
        run('git pull')
