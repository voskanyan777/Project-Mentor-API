from fastapi import FastAPI, Depends
from auth.routers import auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get('/test')
async def test():
    return {"message": "Hello World"}