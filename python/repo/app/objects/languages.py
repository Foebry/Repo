import os

from app.objects.git import Git
from app.objects.licences import chooseLicense
from app.objects.repositories import Repository
from app.objects.packages import Package


class MainClass:
    def __init__(self, app, namespace):
        self.repo = Repository(namespace)
        self.git = Git(app, namespace, self.repo)

    def devBranch(self):
        os.system("git branch develop")
        os.system("git checkout develop")
        os.system("git add *")
        os.system("git push --set-upstream origin develop")


class Python(MainClass):
    def __init__(self, app, namespace):
        super().__init__(app, namespace)
        self.repo.createSetup(app)
        self.package = Package(self.repo, app, self.git)
        self.git.commit(self.repo)
        self.devBranch()


class Dart(MainClass):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.initPackage("dart")
        self.initLocalRepo("dart")
        commit()


class JavaScript(MainClass):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.initPackage("js")
        self.initLocalRepo("js")
        commit()


class C(MainClass):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.initPackage("c")
        self.initLocalRepo("c")
        commit()


class Cs(MainClass):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.initPackage("cs")
        self.initLocalRepo("cs")
        commit()


class Cpp(MainClass):
    def __init__(self, namespace):
        super().__init__(namespace)
        self.initPackage("cpp")
        self.initLocalRepo("cpp")
        commit()


class PHP(MainClass):
    def __init__(self, app, namespace):
        super().__init__(app, namespace)
        self.repo.initPHP()
        self.git.commit(self.repo)
        self.devBranch()


class Web(MainClass):
    def __init__(self, app, namespace):
        super().__init__(app, namespace)
        self.repo.initWeb(app, namespace.new_base)
        self.git.commit(self.repo)
        self.devBranch()
