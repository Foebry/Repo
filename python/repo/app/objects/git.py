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

        self.setup(repo)

        # app.api.postRepository(self.data)

        self.ignore()

    def setup(self, repo):
        """ """

        if "license" not in self.data:
            self.data["license"] = chooseLicense()
        if "description" not in self.data:
            self.data["description"] = input("Give a short description of your package's purpose: \n")

        # create README.md
        README = input("Write your README.md now? (y/n): ")
        if README in ("", "n"):
            confirmation = input("Are you sure you want to write your README file later? (y/n): ")
            if confirmation not in ["", "y"]:
                self.setup(repo)
            README = "# {}".format(repo.name.capitalize())

            with open("README.md", "a+"):
                no_content = file.read() == ("" or "\n")
                if no_content:
                    file.write(README)

        elif README == "y":
            readme_id = None
            done = False
            while done != "y":
                with open("README.md", "a+") as file:
                    # get all process_ids for all open notepads
                    notepads = [proc.pid for proc in psutil.process_iter() if proc.name() == "notepad.exe"]

                    # open new notepad window if our readme.md is not open (yet)
                    if not done and readme_id not in notepads:
                        os.startfile(os.path.join("README.md"))

                        # get id and process for our readme.md
                        readme_id, proc = [
                            [proc.pid, proc]
                            for proc in psutil.process_iter()
                            if proc.name() == "notepad.exe" and proc.pid not in notepads
                        ][0]

                done = input("Done creating README.md file? (y/n): ")

            if readme_id in [proc.pid for proc in psutil.process_iter() if proc.name() == "notepad.exe"]:
                proc.kill()

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
