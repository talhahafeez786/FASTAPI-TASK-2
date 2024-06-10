from fastapi import FastAPI
from views import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the user management system!"}
