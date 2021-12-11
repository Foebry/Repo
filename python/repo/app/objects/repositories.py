import os

from app.objects.base import createBaseFolder, findBaseFolder


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

        if new_basefolder or (app.basefolder in ("FULL_PATH_TO_YOUR_STANDARD_BASE_FOLDER_CSS", "")):
            print("You have not set any default base folder yet..")
            ref_base = createBaseFolder(app)

        target = os.path.join(self.path, "css", "base")

        # check if location of ref_base exists
        if not os.path.isdir(ref_base):
            print("The location of your base folder in the config file does not exist...")
            ref_base = findBaseFolder(app)

        ref_base = ref_base.replace("//", "\\")
        os.system(f"xcopy {ref_base} {target} /E")

    def initPHP(self):
        """ """

        os.system("cd .> main.php")

    def createLicense(self, app, license):
        os.system("cd .> license.MD")
        license = app.api.getLicenses()[license][license]
        with open("license.MD", "w") as file:
            file.write(app.api.getLicense(license, ("body",)))
