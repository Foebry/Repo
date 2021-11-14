#!/usr/bin/env python

import argparse
import os
import sys
import json

from app.objects.languages import Python, Web, PHP
from pathlib import Path
from app.app import App
from app.help import help

this = (Path(__file__).resolve().parent)

parser = argparse.ArgumentParser(
)
parser.add_argument("--name", "-n", type=str, dest="name", required=True, help="Name of your project and repository")
parser.add_argument("--private", "-p", dest="is_private", action='store_true', help="leave flag off for public or put flag on for private repository")
parser.add_argument("--lan", type=str, dest="language", required=True, help="main language of the project")
parser.add_argument("--branch", type=str, default="main", dest="branch")


try:
    if '-h' in sys.argv or '--help' in sys.argv:
        help()
        quit()
    elif len(sys.argv) < 5: print("For help type repo.py -h\n\n")

    args = parser.parse_args()
    with open(os.path.join(this, "config.json")) as file:
        data = json.load(file)
        app = App(data)

        languages = {
            "py": Python,
            "web": Web,
            "php": PHP
        }
        languages[args.language.lower()](app, args)

except Exception as e:
    print(e)
