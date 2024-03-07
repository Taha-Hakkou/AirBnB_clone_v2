#!/usr/bin/python3
""" 1-pack_web_static: (fabric script) """
from fabric.api import local
import time


def do_pack():
    """ generates a .tgz archive from the contents
    of the web_static folder of the AirBnB_clone_v2 repo """
    local("if [ ! -e versions/ ]; then mkdir versions; fi")
    archive_path = f"versions/web_static_{time.strftime('%Y%m%d%H%M%S')}.tgz"
    packing = local(f"tar -cvzf {archive_path} web_static")
    if packing.succeeded:
        return (archive_path)
    return (None)
