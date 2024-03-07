#!/usr/bin/python3
""" 2-do_deploy_web_static: (fabric script) """
from fabric.api import *
import os.path

env.hosts = ['100.26.155.232', '54.237.90.253']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if not os.path.exists(archive_path):
        return (False)
    try:
        put(archive_path, "/tmp/")
        static_path = archive_path.split('/')[1].split('.')[0]
        run(f"mkdir -p /data/web_static/releases/{static_path}/")
        run(f"tar -xzf /tmp/{static_path}.tgz -C \
/data/web_static/releases/{static_path}/")
        run(f"rm -rf /tmp/{static_path}/")
        run(f"mv /data/web_static/releases/{static_path}/web_static/* \
/data/web_static/releases/{static_path}/")
        run(f"rm -rf /data/web_static/releases/{static_path}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{static_path}/ \
/data/web_static/current")
        # New version deployed!
        return (True)
    except Exception:
        return (False)
