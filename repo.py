#!/usr/bin/env python

from secrets import GITHUB_TOKEN
import requests
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private

url = "https://api.github.com/user/repos"
if is_private: payload = '{"name": "' + repo_name + '", "private": true}'
else: payload = '{"name": "' + repo_name + '", "private": false}'

headers = {
    "Authorization": 'token '+GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}


response = requests.post(url, data=payload, headers=headers)

try:
    REPO_PATH = os.getcwd()
    print(REPO_PATH)
    os.chdir(REPO_PATH)
    os.system("mkdir " + repo_name)
    os.chdir(f'{REPO_PATH}/{repo_name}')
    os.system("git init")
    os.system("git remote add origin https://github.com/Foebry/" + repo_name)
    os.system("echo '# " + repo_name + "' >> README.md")
    os.system("echo '# " + repo_name + "' >> .gitignore")
    os.system('python -m venv env')
    os.system('git add . && git commit -m "Initial commit" && git push origin master')
except FileExistsError as error: pass
