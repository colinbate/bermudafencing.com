from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env
from fabric.contrib.console import confirm

env.hosts = ['cbate.com']

def deploy():
	site_dir = '/var/www/bermudafencing.com'
	with cd(site_dir):
		run("hg pull -u")