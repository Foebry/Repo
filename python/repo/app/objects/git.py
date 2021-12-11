import os
import json

from app.objects.licences import chooseLicense


class Git:
    """
    representation of git.

    """

    def __init__(self, app, namespace, repo):
        """
        initialize git repository
        """
        # create github repository
        self.data = {
            "name": namespace.name,
            "private": str(namespace.is_private).lower(),
        }

        os.system("git init")
        os.system("git remote add origin https://github.com/%s/%s.git" % (app.profile, namespace.name))
        os.system("git branch -M main")

        self.setup(repo, app)
        self.data["license"] = ""
        app.api.postRepository(self.data)

        self.ignore()

    def setup(self, repo, app):
        """ """

        if "license" not in self.data:
            licenses = app.api.getLicenses()
            self.data["license"] = chooseLicense(app)
            if self.data["license"] > -1:
                repo.createLicense(app, self.data["license"])

        if "description" not in self.data:
            self.data["description"] = input("Give a short description of your package's purpose: \n")

        # create README.md
        README = input("Write your README.md now? (y/n): ").lower()
        if README in ("", "n"):
            confirmation = input("Are you sure you want to write your README file later? (y/n): ").lower()
            if confirmation not in ["", "y"]:
                return self.setup()
            README = "# {}".format(repo.name.capitalize())

            with open("README.md", "a") as file:
                file.write(README)

        elif README == "y":
            done = False
            while done != "y":
                with open("README.md", "a+") as file:
                    os.startfile(os.path.join("README.md"))
                done = input("Done creating README.md file? (y/n): ").lower()

        else:
            return self.setup(repo)

    def ignore(self):
        """
        create .gitignore
        """
        IGNORE = """
/env
/logs
/Logs
.log
__pycache__
config.json
    """
        file = open(".gitignore", "w")
        file.write(IGNORE)
        file.close()

    def commit(self, repo):
        os.chdir(repo.path)
        os.system("git add .")
        os.system('git commit -m "initial commit"')
        os.system("git push --set-upstream origin main")
