from app.api import API


class App:
    """ """

    def __init__(self, data, root):
        self.email = data["INFO"]["EMAIL"]
        self.name = data["INFO"]["NAME"]
        self.security = data["APP"]["security"]
        self.token = data["APP"]["CREDENTIALS"]["GITHUB_TOKEN"]
        self.profile = data["APP"]["CREDENTIALS"]["GITHUB_PROFILE"]
        self.basefolder = data["APP"]["WEB_BASE_FOLDER"]
        self.api = API(data["APP"])
        self.root = root
