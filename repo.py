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
    os.chdir(REPO_PATH)
    os.system("mkdir " + repo_name)
    parent_path = f'{REPO_PATH}/{repo_name}'
    os.chdir(f'{parent_path}')
    os.system("git init")
    os.system("git remote add origin https://github.com/Foebry/" + repo_name)
    os.system("echo. > README.md")
    os.system(f'python -m venv {repo_name}')
    # create .gitignore
    os.system("echo __pycache__ >> .gitignore")
    os.system("echo /Logs/* >> .gitignore")
    os.system("echo *.log >> .gitignore")
    # create setup.py
    os.system("echo from setuptools import setup >> setup.py")
    os.system("echo setup( >> setup.py")
    os.system(f"echo     name = '{repo_name}', >> setup.py")
    os.system("echo     version = 0.1, >> setup.py")
    os.system("echo     packages = [], >> setup.py")
    os.system(f"echo     url = 'https://github.com/Foebry/{repo_name}', >> setup.py")
    os.system("echo     author = 'Foebry', >> setup.py")
    os.system("echo     author_email = 'rain_fabry@hotmail.com', >> setup.py")
    os.system("echo     description = '' >> setup.py")
    os.system("echo ) >> setup.py")
    # setting git settings
    os.system('git config --global user.email "rain_fabry@hotmail.com"')
    os.system('git config --global user.name "Foebry"')
    os.system('git add . && git commit -m "Initial commit" && git push origin master')
    # adding parent_path to pythonpath environment variable
    os.system(f"setx pythonpath='%pythonpath%;{parent_path}'")
    os.system("python -m pip install --upgrade pip")
except FileExistsError as error: print(f"A folder with name {repo_name} already exists")
except Exception as error: print(type(error), error)
