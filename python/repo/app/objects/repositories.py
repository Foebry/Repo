import os
import easygui
import json


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
        ref_base = app.basefolder
        if new_basefolder or (
            app.basefolder in ("FULL_PATH_TO_YOUR_STANDARD_BASE_FOLDER_CSS", "")
        ):
            ref_base = self.createBaseFolder(app)
        target = os.path.join(self.path, "css", "base")
        if not os.path.isdir(ref_base):
            print(
                "The location of your base folder in the config file does not exist..."
            )
            ref_base = self.findBaseFolder(app)
        ref_base = ref_base.replace("//", "\\")
        os.system(f"xcopy {ref_base} {target} /E")

    def findBaseFolder(self, app):
        print(
            "Please select the correct location of your base folder, cancel to create a new base folder"
        )
        folder = easygui.diropenbox()
        if folder is None:
            print("No base folder selected, creating new base folder")
            return self.createBaseFolder(app)
        self.saveBaseFolder(app, folder)
        return folder

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
        self.saveBaseFolder(app, new_folder)
        return new_folder

    def saveBaseFolder(self, app, new_folder):
        new_folder = new_folder.replace("\\", "//")
        with open(os.path.join(app.root, "config.json"), "r") as file:
            lines = file.readlines()
        new_lines = []
        for line in lines:
            if "WEB_BASE_FOLDER" in line:
                pos = line.find(":")
                line = line.replace(line[pos:], f':"{new_folder}",')
            new_lines.append(line)
        text = "".join(new_lines)

        with open(os.path.join(app.root, "config.json"), "w") as file:
            config = json.loads(text)
            json.dump(config, file, indent=4)

    def initPHP(self):
        """ """

        os.system("cd .> main.php")
