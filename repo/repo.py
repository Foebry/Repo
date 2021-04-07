import os
import Git
import json
import base64

from secrets import GITHUB_PROFILE, EMAIL, NAME



class Repo:

    def __init__(self, namespace):
        from Git import init, commit
        """ Creating a brand new github repository with python package"""
        self.private = namespace.is_private
        self.name = namespace.name
        self.branch = namespace.branch
        self.env = namespace.env
        if self.env == self.name.lower(): self.env = '_'+self.env

        repo = os.path.join(os.getcwd(), self.name)
        package = os.path.join(repo, self.name.lower())

        # create local folder package inside repo
        os.system("mkdir %s" %package)
        os.chdir(repo)

        # initialize github repository
        init(self.name, self.private)

        # initialize package
        os.chdir(package)
        self.initPackage()

        # initialize local repo
        os.chdir(repo)
        self.initLocalRepo()

        self.createVirtualEnvironment()

        # commit changes and push to Github
        os.chdir(repo)
        commit()



    def createVirtualEnvironment(self):
        import os
        print("creating venv %s" %self.env)
        os.system("python -m venv %s" %self.env)
        env_path = os.path.join(os.getcwd(),'%s','scripts') %self.env
        os.chdir(env_path)
        os.system("activate")
        os.system("python -m pip install --upgrade pip")
        os.system("deactivate")



    def initPackage(self):
        os.system("cd .> __init__.py")
        os.system("cd .> main.py")
        self.createVersion()


    def createVersion(self):
        from datetime import datetime as dt
        from Git import chooseLicense
        from secrets import NAME, EMAIL, GITHUB_PROFILE

        license = chooseLicense()
        description = input("Give a short description of your package's purpose: \n")
        url = input("Any website for you package? if No press enter\n")

        content =\
"""
__title__ = '%s'
__description__ = '%s'
__url__ = '%s'
__version__ = '0.0.1'
__author__ = '%s'
__author_email__ = '%s'
__license__ = '%s'
__copyright__ = 'Copyright %s %s'
""" %(self.name.lower(), description, url, GITHUB_PROFILE, EMAIL, license, dt.now().year, NAME)

        file = open("__version__.py", 'w')
        file.write(content)
        file.close



    def initLocalRepo(self):
        from Git import ignore
        # create README.md
        README = input("Write your README.md file here. Press enter if you want to do it later.:\n")
        if README == "":
            confirmation = input("Are you sure you want to write your README file later? (y/n): ")
            if confirmation not in ["", "y"]: self.initLocalRepo()

        os.system("cd . > config.py")
        os.system("cd .> config_ex.py")
        file = open("README.md", "w")
        file.write(README)
        file.close()

        self.setup()
        ignore()



    def setup(self):
        import os
        from secrets import GITHUB_PROFILE

        SETUP = \
"""
import os

from codecs import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['%s']

requires = []

about = {}
with open(os.path.join(here, '%s', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'%s': '%s'},
    include_package_data=True,
    install_requires=requires,
    license=about['__license__'],
    project_urls={
        'Source': 'https://github.com/%s/%s',
    },
)
""" %(self.name.lower(), self.name.lower(), self.name.lower(), self.name.lower(), GITHUB_PROFILE, self.name)

        file = open("setup.py", "w")
        file.write(SETUP)
        file.close()

        os.system("cd .> setup.cfg")
