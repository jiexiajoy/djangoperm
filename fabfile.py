#! -*- coding: utf-8 -*-

from __future__ import with_statement
from itertools import dropwhile
from fabric.api import *
from fabric.colors import *
from fabric.contrib.console import *


env.local_src_dir = '/Users/manmanli/xm-webs/djangoperm/'


@runs_once
def prepare_deploy():
    with lcd(env.local_src_dir):
        local('git add -A')
        local('git commit -m "djangoperm"')
        local('git push')
