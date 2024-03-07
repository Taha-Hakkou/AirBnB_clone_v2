#!/usr/bin/python3
""" 3-deploy_web_static: (fabric script) """
from fabric.api import *
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


env.hosts = ['100.26.155.232', '54.237.90.253']
env.user = 'ubuntu'

def deploy():
    """ creates and distributes an archive to your web servers """
    archive_path = do_pack()
    if archive_path.failed:
        return (False)
    dp = do_deploy(archive_path)
    return (dp)
