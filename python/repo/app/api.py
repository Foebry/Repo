from requesting.users import User

import ast

class API:
    """

    """
    def __init__(self, data):
        self.user = User(data)
        self.user.authenticate(data["CREDENTIALS"]["GITHUB_TOKEN"])


    def postRepository(self, data):
        """

        """

        payload = '{"name": "' + data["name"] + '", "private": false}'
        data = "{" + ", ".join(f'"{key}": "{data[key]}"' for key in data) + "}"
        data = data.replace('"false"', 'false').replace("'true'", 'true')

        endpoint = "{}/user/repos".format(self.user.endpoint)
        headers = {
            "Authorization": 'token '+ self.user.access_token,
            "Accept": "application/vnd.github.v3+json"
        }
        return self.user.post(endpoint, headers, data)
