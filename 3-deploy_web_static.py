#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import *
from datetime import datetime
import os


# env.user = "ubuntu"
env.hosts = ['52.90.14.190', '18.206.202.178']


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


def do_deploy(archive_path):
    """
        Distribute an archive to your web servers, using the function
        do_deploy.
    """
    if os.path.exists(archive_path):
        archive_file = archive_path[9:]
        server_version = "/data/web_static/releases/" + archive_file[:-4]
        archive_file = "/tmp/" + archive_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(server_version))
        run("sudo tar -xzf {} -C {}/".format(archive_file,
                                             server_version))
        run("sudo rm {}".format(archive_file))
        run("sudo mv {}/web_static/* {}".format(server_version,
                                                server_version))
        run("sudo rm -rf {}/web_static".format(server_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(server_version))

        print("Server version deployed!")
        return True

    return False


def deploy():
    """Creates the pack and deploys it!!!"""
    archive_p = do_pack()
    if os.path.exists(archive_p):
        return do_deploy(archive_p)
    return false
