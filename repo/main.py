#!/usr/bin/env python

from secrets import GITHUB_TOKEN
import requests
import argparse
import os
import sys

__doc__ = """
The correct usage is: py E:/Projects/Python/repo/repo/main.py --name '' --private --lan '' --env '' --branch ''\n
arguments are \n
--name: package or project name -> required
--lan: extension of language you want your project or package to be -> required
--private tag -> optional
--env: name of environment only for py -> optional
--branch: name of branch -> optional"""


parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action='store_true')
parser.add_argument("--lan", type=str, dest="language", required=True)
parser.add_argument("--env", type=str, dest="env", default='env')
parser.add_argument("--branch", type=str, dest="branch", default='master')

try:
    args = parser.parse_args()
except:
    print(__doc__)
    quit()

if args.language == "py":
    from repo import Python
    Python(args)
    quit()
