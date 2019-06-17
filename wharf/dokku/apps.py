from wharf.dokku.base import BaseController


class AppController(BaseController):
    def __init__(self, client: 'wharf.dokku.DokkuDaemonClient', app: str):
        super().__init__(client)
        self.app = app

    async def exists(self):
        res = await self.client.call("apps:exists", self.app)
        return res["ok"]

    async def create(self):
        if await self.exists():
            raise AppExistsException(f"Application {self.app} already exists")
        res = await self.client.call("apps:create", self.app)
        return res["ok"]

    def __str__(self):
        return f"AppController(app={self.app})"


class AppExistsException(Exception):
    pass


class AppDoesNotExistsException(Exception):
    pass
