#!/usr/bin/python

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import xldeploy
repo = xldeploy.connect_repository()

try:
    origin_package = sys.argv[1]
    destination_package = sys.argv[2]
    ci_name = sys.argv[3]
    new_ci_name = sys.argv[4]
except Exception:
    print "invalid number of arguments: <origin_package> <destination_package> <ci_name> <new_ci_name>"


origin_ci = repo.get_ci_by_name("%s/%s" % (origin_package, ci_name))

cloned_ci = origin_ci.clone("%s/%s" % (destination_package, new_ci_name))


repo.save_ci(cloned_ci)