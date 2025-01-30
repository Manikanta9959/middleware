from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(
    GZipMiddleware,
    minimum_size = 100
)


@app.get("/")
async def test():
    return {
        "test" :"ok"
    }
    

@app.get("/zip")
async def gzip():
    val = "0998" * 500
    return {
        "value" : val
    }
