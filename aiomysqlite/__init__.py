from asqlite import connect

async def create_pool(filename):
    return Pool(filename)

class Pool:
    def __init__(self, filename):
        self.filename = filename

    def acquire(self):
        return PoolAcquireContextManager(self.filename)

class PoolAcquireContextManager:
    def __init__(self, filename):
        self.filename = filename

    async def __aenter__(self):
        self.connection = await connect(self.filename)
        return self.connection

    async def __aexit__(self, *args, **kwargs):
        await self.connection.close()
