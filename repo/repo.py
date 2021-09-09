import os
import Git

from secrets import GITHUB_PROFILE, EMAIL, NAME
from Git import init, commit, ignore, chooseLicense
from datetime import datetime as dt



class MainClass():

    def __init__(self, namespace):

        self.private = namespace.is_private
        self.name = namespace.name
        self.branch = namespace.branch
        self.repo = os.path.join(os.getcwd(), self.name)
        self.package = os.path.join(self.repo, self.name.lower())

        os.system("mkdir {}".format(self.package))
        os.chdir(self.repo)
        init(self.package, self.name, self.private)


    def initPackage(self, ext):
        os.system("cd .> __init__.{}".format(ext))
        os.system("cd .> main.{}".format(ext))
        self.createVersion()
        os.chdir(self.repo)


    def initLocalRepo(self, ext):
        # create README.md
        README = input("Write your README.md file here. Press enter if you want to do it later.:\n")
        if README == "":
            confirmation = input("Are you sure you want to write your README file later? (y/n): ")
            if confirmation not in ["", "y"]: self.initLocalRepo()

        os.system("cd . > config.{}".format(ext))
        os.system("cd .> config_ex.{}".format(ext))
        file = open("README.md", "w")
        file.write(README)
        file.close()

        self.setup()
        ignore()
        os.chdir(self.repo)



class Python(MainClass):

    def __init__(self, namespace):
        super().__init__(namespace)
        self.initPackage('py')
        self.initLocalRepo('py')
        commit()


    def createVersion(self):

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

        os.system("cd .> changelog.log")



class Dart(MainClass):

    def __init__(self, namespace):
        super.__init__(namespace)
        self.initPackage('dart')
        self.initLocalRepo('dart')
        commit()


class JavaScript(MainClass):

    def __init__(self, namespace):
        super.__init__(namespace)
        self.initPackage('js')
        self.initLocalRepo('js')
        commit()



class C(MainClass):

    def __init__(self, namespace):
        super.__init__(namespace)
        self.initPackage('c')
        self.initLocalRepo('c')
        commit()



class Cs(MainClass):

    def __init__(self, namespace):
        super.__init__(namespace)
        self.initPackage('cs')
        self.initLocalRepo('cs')
        commit()



class Cpp(MainClass):

    def __init__(self, namespace):
        super.__init__(namespace)
        self.initPackage('cpp')
        self.initLocalRepo('cpp')
        commit()
