from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from model import InputData
from text2Speech import text2Speech
import sys

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


@app.post("/inputText/")
async def text_to_speech_endpoint(input_data: InputData):
    return await text2Speech(input_data)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)