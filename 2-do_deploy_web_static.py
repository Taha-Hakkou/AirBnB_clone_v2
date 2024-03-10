#!/usr/bin/python3
""" 2-do_deploy_web_static: (fabric script) """
from fabric.api import *
import os.path
import time

env.hosts = ['100.26.155.232', '54.237.90.253']
env.user = 'ubuntu'


def do_pack():
    """ generates a .tgz archive from the contents
    of the web_static folder of the AirBnB_clone_v2 repo """
    local("if [ ! -e versions/ ]; then mkdir versions; fi")
    archive_path = f"versions/web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz"
    packing = local(f"tar -cvzf {archive_path} web_static")
    if packing.succeeded:
        return (archive_path)
    return (None)


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return (False)
    try:
        put(archive_path, "/tmp/")
        static_path = archive_path.split('/')[1].split('.')[0]
        releases = '/data/web_static/releases'
        current = '/data/web_static/current'
        run(f"mkdir -p {releases}/{static_path}/")
        run(f"tar -xzf /tmp/{static_path}.tgz -C {releases}/{static_path}/")
        run(f"rm -rf /tmp/{static_path}/")
        run(f"mv {releases}/{static_path}/web_static/* \
{releases}/{static_path}/")
        run(f"rm -rf {releases}/{static_path}/web_static")
        run(f"rm -rf {current}")
        run(f"ln -s {releases}/{static_path}/ {current}")
        print('New version deployed!')
        return (True)
    except Exception:
        return (False)
