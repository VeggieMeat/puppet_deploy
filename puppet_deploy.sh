#!/bin/bash
#
# Fabfile wrapper script
#

# Fabfile location
FABFILE=/usr/local/bin/puppet_deploy/fabfile.py

LIST=$1
MASTER=$2

exec < $LIST
while read LINE
  do
    HOSTS=$HOSTS','$LINE
  done

HOSTLIST=$(echo $HOSTS | awk '{print substr($0,2)}')
fab -f $FABFILE -H $HOSTLIST puppet:master=$MASTER || exit 1
