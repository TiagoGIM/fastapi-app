from fastapi import FastAPI
from app.controllers.item_controller import router as item_router
from app.user.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router,prefix="/api")
app.include_router(item_router, prefix="/api")



@app.get("/")
def read_root():
    return "wellcome go to /docs and have fun"
