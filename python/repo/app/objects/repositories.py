import os
import easygui


class Repository:
    def __init__(self, namespace):
        self.name = namespace.name
        self.path = os.path.join(os.getcwd(), self.name)
        os.system(f"mkdir {self.path}")
        os.chdir(self.path)

    def createSetup(self, app):

        SETUP = """
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
""" % (
            self.name.lower(),
            self.name.lower(),
            self.name.lower(),
            self.name.lower(),
            app.profile,
            self.name,
        )

        file = open("setup.py", "w")
        file.write(SETUP)
        file.close()

    def initWeb(self, app, new_basefolder):
        """ """
        os.system("mkdir +assets, css, images")
        os.system("cd .> index.html")
        os.chdir(os.path.join(self.path, "css"))
        os.system("cd .> style.scss")
        os.system("mkdir base")
        if new_basefolder or app.basefolder in (
            "FULL_PATH_TO_YOUR_STANDARD_BASE_FOLDER_CSS",
            "",
        ):
            ref_base = self.createBaseFolder(app)
        target = os.path.join(self.path, "css", "base")
        os.system(f"xcopy {ref_base} {target} /E")

    def createBaseFolder(self, app):
        print(
            "please select the location where you would like to store you reference base folder"
        )
        folder = easygui.diropenbox()
        os.chdir(folder)
        new_folder = os.path.join(folder, "base")
        os.system(f"mkdir {new_folder}")
        os.chdir(new_folder)
        os.system("cd .> _reset.scss")
        os.system("cd .> _extends.scss")
        os.system("cd .> _fonts.scss")
        os.system("cd .> _mixins.scss")
        os.system("cd .> _variables.scss")
        open_file = open(os.path.join(app.root, "config.json"), "r")
        lines = open_file.readlines()
        open_file.close()
        with open(os.path.join(app.root, "config.json"), "w") as config:
            for line in lines:
                if "WEB_BASE_FOLDER" in line:
                    line = f'"WEB_BASE_FOLDER": "{new_folder}",'
                config.write(line)
        return new_folder

    def initPHP(self):
        """ """

        os.system("cd .> main.php")
