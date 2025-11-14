import aiosqlite

class Database():
    def __init__(self): raise NotImplementedError("NOT IMPLEMENTED")
    async def connect(self, name: str): raise NotImplementedError("NOT IMPLEMENTED")
    async def disconnect(self): raise NotImplementedError("NOT IMPLEMENTED")
    class QueryType(): NONE = 0; FETCH_ONE = 1; FETCH_ALL = 2;
    async def query(self, query: str, params = None, query_type = QueryType.NONE) -> tuple | None: raise NotImplementedError("NOT IMPLEMENTED")

class SqliteDB(Database):
    QueryType = Database.QueryType
    
    def __init__(self, name: str = None):
        self.con: aiosqlite.Connection = None
        self.db_name: str = name

    async def connect(self, name: str):
        self.con = await aiosqlite.connect(name)
        self.db_name = None
        return self
    
    async def disconnect(self):
        if(self.con): await self.con.close()

    async def query(self, query: str, params = None, query_type = QueryType.NONE):
        cursor = await self.con.execute(query, params)

        ret = None
        match(int(query_type)):
            case int(self.QueryType.NONE): return
            case int(self.QueryType.FETCH_ONE): ret = (await cursor.fetchone())[0]
            case int(self.QueryType.FETCH_ALL): ret = await cursor.fetchall()
        
        return ret

    async def __aenter__(self):
        if(self.db_name): 
            await self.connect(self.db_name)
        return self

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        if(self.con): await self.con.close()
