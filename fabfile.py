#! -*- coding: utf-8 -*-

from __future__ import with_statement
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import *


env.local_src_dir = '/Users/manmanli/xm-webs/djangoperm/'


@runs_once
def prepare_deploy():
    with lcd(env.local_src_dir):
        with warn_only():
            result = local('git add -A', capture=True).succeeded and local('git commit -m "djangoperm"', capture=True).succeeded and local('git push', capture=True).succeeded
            if result:
                abort(red(output.stderr))
