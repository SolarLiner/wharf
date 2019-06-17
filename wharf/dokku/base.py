from wharf.dokku import DokkuDaemonClient


class BaseController:
    def __init__(self, client: DokkuDaemonClient):
        self.client = client

    def _client_send(self, data=None):
        return self.client.send(data)

    def _client_send_sync(self, data=None):
        return self.client.send_sync(data)
