import os



class Repository:

    def __init__(self, namespace):
        self.name = namespace.name
        self.path = os.path.join(os.getcwd(), self.name)
        os.system(f"mkdir {self.path}")
        os.chdir(self.path)


    def createSetup(self, app):

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
""" %(self.name.lower(), self.name.lower(), self.name.lower(), self.name.lower(), app.profile, self.name)

        file = open("setup.py", "w")
        file.write(SETUP)
        file.close()



    def initWeb(self):
        """

        """
        os.system("mkdir +assets, css, images")
        os.system("cd .> css/reset.css")
        os.system("cd .> css/style.css")
        os.system("cd .> index.html")


    def initPHP(self):
        """

        """

        os.system("cd .> main.php")
