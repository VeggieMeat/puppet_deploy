from fabric.api import *

def puppet(master):
  run("sudo puppet agent --server=%s --no-daemonize --onetime --verbose", %(master))
