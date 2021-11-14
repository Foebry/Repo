import os

from datetime import datetime as dt


class Package:

    def __init__(self, repo, app, git):
        self.name = repo.name
        self.path = os.path.join(repo.path, self.name)
        os.system(f"mkdir {self.path}")
        os.chdir(self.path)
        os.system("cd .> __init__.py")
        os.system("cd .> main.py")
        self.createVersion(git, app)


    def createVersion(self, git, app):
        content = \
"""
__title__ = '%s'
__description__ = '%s'
__version__ = '0.0.1'
__author__ = '%s'
__author_email__ = '%s'
__copyright__ = 'Copyright %s %s'
""" %(git.data["name"].lower(), git.data["description"], app.profile, app.email, dt.now().year, app.name)

        file = open("__version__.py", 'w')
        file.write(content)
        file.close

        os.system("cd . > config.json")
        os.system("cd .> config_ex.json")
