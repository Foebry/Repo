from requesting.users import User
import requests
import json


class API:
    """ """

    def __init__(self, data):
        self.user = User(data)
        self.user.authenticate(data["CREDENTIALS"]["GITHUB_TOKEN"])

    def postRepository(self, data):
        """ """

        payload = '{"name": "' + data["name"] + '", "private": false}'
        data = "{" + ", ".join(f'"{key}": "{data[key]}"' for key in data) + "}"
        data = data.replace('"false"', 'false').replace("'true'", 'true')

        endpoint = "{}/user/repos".format(self.user.endpoint)
        headers = {"Authorization": 'token ' + self.user.access_token, "Accept": "application/vnd.github.v3+json"}
        return self.user.post(endpoint, headers, data)

    def getLicenses(self):
        endpoint = self.user.endpoint + "/licenses"
        headers = {"Authorization": 'token ' + self.user.access_token, "Accept": "application/vnd.github.v3+json"}
        data = self.user.get(endpoint, headers=headers)

        return [{data.index(row): row["key"], "name": row["name"]} for row in data]

    def getLicense(self, license_key, request_data=None):

        endpoint = f"{self.user.endpoint}/licenses/{license_key}"
        headers = {"Authorization": 'token ' + self.user.access_token, "Accept": "application/vnd.github.v3+json"}

        return self.user.get(endpoint, headers=headers, request_data=request_data)
