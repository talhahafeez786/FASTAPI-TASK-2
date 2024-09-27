from fastapi import FastAPI
from app.views import router  # Corrected import

app = FastAPI()

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the user management system!"}
