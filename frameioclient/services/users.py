from typing import Dict

from ..lib.service import Service


class User(Service):
    def get_me(self):
        """
        Get the current user.
        """
        return self.client._api_call("get", "/me")

    def get_accounts(self):
        """
        Get a list of accounts the user has access to
        """
        return self.client._api_call("get", "/accounts")

    def get_shared_projects(self):
        """
        Get a list of projects the user has been added as a collaborator to
        """
        return self.client._api_call("get", "/projects/shared")
