from fabric.api import *
env.user = 'bender'
env.shell = '/bin/bash -c'

@parallel
def puppet(master):
  run("sudo puppet agent --server=%s --no-daemonize --onetime --verbose" %(master))
