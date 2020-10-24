'''
Created on 10 Oct 2020

@author: info
'''
import atexit
import subprocess
from setuptools.command.install import install

def _post_install():
    subprocess.call(["systemctl","enable","servo-control"])
    subprocess.call(["systemctl","daemon-reload"])

class NewInstall(install):
    def __init__(self, *args, **kwargs):
        super(NewInstall, self).__init__(*args, **kwargs)
        atexit.register(_post_install)