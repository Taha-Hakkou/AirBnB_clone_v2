#!/usr/bin/python3
""" 100-clean_web_static: (fabric script) """
from fabric.api import *


env.hosts = ['100.26.155.232', '54.237.90.253']
env.user = 'ubuntu'

def do_clean(number=0):
    """ deletes out-of-date archives """
    if number == 0:
        number = 1
    local(f"rm $(ls -C | head -n $( $(ls -1 | wc -l) - {number}))")
    with cd("/tmp/"):
        run(f"rm $(ls -C | head -n $( $(ls -1 | wc -l) - {number}))")
