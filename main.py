import fastapi as f
import asyncio
from api import account, payment, cors

app = f.FastAPI()
cors.attach_middleware(app)

account_manager = account.AccountManager()
app.include_router(account_manager.router)
 
@app.get("/ping")
async def ping(request: f.Request):
    #print(request.client)
    print("Hello")
    await asyncio.sleep(5)
    print("bye")
    return "pong"
