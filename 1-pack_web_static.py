#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
i"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ creates a directory and put the compress webstatic into it"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_fpath = "versions/web_static_{}.tgz".format(date)
    t_gzip_arc = local("tar -cvzf {} web_static".format(archived_fpath))

    if t_gzip_arc.succeeded:
        return archived_fpath
    else:
        return None
