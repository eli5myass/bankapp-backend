from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

origins = [
    "http://localhost",
    "http://localhost:8080",
    # MORE TO ADD HERE
]

def attach_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )