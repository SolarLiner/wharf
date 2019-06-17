import asyncio
import json

import socket

from wharf.dokku.apps import AppExistsException
from .apps import AppController


class DokkuDaemonClient:
    def __init__(self, addr="/var/run/dokku-daemon/dokku-daemon.sock"):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(addr)

    async def get_app(self, app: str):
        return AppController(self, app)

    async def call(self, *params: str):
        return self.send('"' + '" "'.join(params))

    async def send(self, data=None):
        self.socket.sendall(bytes(data))
        recv = ""
        while not recv.endswith("\n"):
            recv += self.socket.recv(512).decode("utf-8")
        return json.loads(recv)

    def send_sync(self, data=None):
        return asyncio.get_event_loop().run_until_complete(asyncio.run(self.send(data)))

    def __call__(self, *args, **kwargs):
        return self.call(*args)
