#!/usr/bin/env python
from __future__ import print_function

import argparse
import os
import sys

from nose.core import run


# This is a whitelist of unit tests that support Python 3.
# When porting a new module to Python 3, please update this
# list so that its tests will run by default. See the
# `default` target below for more information.
# We use this instead of test attributes/tags because in
# order to filter on tags nose must load each test - many
# will fail to import with Python 3.
PY3_WHITELIST = ()


def main(whitelist=[]):
    description = ("Runs unit and/or integration tests. "
                   "Arguments will be passed on to nosetests. "
                   "See nosetests --help for more information.")
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-t', '--service-tests', action="append", default=[],
                        help="Run tests for a given service.  This will "
                        "run any test tagged with the specified value, "
                        "e.g -t s3 -t ec2")
    known_args, remaining_args = parser.parse_known_args()
    attribute_args = []
    for service_attribute in known_args.service_tests:
        attribute_args.extend(['-a', '!notdefault,' + service_attribute])
    if not attribute_args:
        # If the user did not specify any filtering criteria, we at least
        # will filter out any test tagged 'notdefault'.
        attribute_args = ['-a', '!notdefault']

    # Set default tests used by e.g. tox. For Py2 this means all unit
    # tests, while for Py3 it's just whitelisted ones.
    if 'default' in remaining_args:
        # Run from the base project directory
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        for i, arg in enumerate(remaining_args):
            if arg == 'default':
                if sys.version_info[0] == 3:
                    del remaining_args[i]
                    remaining_args += PY3_WHITELIST
                else:
                    remaining_args[i] = 'tests/unit'

    all_args = [__file__] + attribute_args + remaining_args
    print("nose command:", ' '.join(all_args))
    if run(argv=all_args):
        # run will return True is all the tests pass.  We want
        # this to equal a 0 rc
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())