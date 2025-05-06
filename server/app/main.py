from fastapi import FastAPI
import uvicorn
from fastapi.testclient import TestClient
from .routers.endpoints import router
from .database.database import engine

app = FastAPI()
app.title = "School"
app.include_router(router=router)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

# def create_user():
#     Base.metadata.create_all(bind=engine)

# create_user()


if __name__ == "__main__":
    uvicorn.run("main:app")