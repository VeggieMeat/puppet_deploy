from fabric.api import *

@parallel
def puppet(master):
  run("sudo puppet agent --server=%s --no-daemonize --onetime --verbose", %(master))
