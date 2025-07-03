import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.endpoints import users_router, subjects_router

app = FastAPI()
app.title = "School"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "School management software"}


app.include_router(router=users_router)
app.include_router(router=subjects_router)

if __name__ == "__main__":
    # app()
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)