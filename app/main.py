from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import post, user, auth, vote
from app.models import Base as models_Base
from app.database import engine
from app.config import settings

# Initialize tables.
models_Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost", "http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "hello world"}
