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
        with warn_only():
            commands = ['git add -A', 'git commit -m "djangoperm"', 'git push']
            for res in dropwhile(lambda command: local(command).return_code in (0, 1), commands):
                abort(red(res))
        print green('-- prepare_deploy success.')
