from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

#cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# custom middleware for logging req and res
class Logging(BaseHTTPMiddleware):
    async def dispatch(self, request : Request, call_next):
        print(">>>>>>>>>0998>>>>>>>0998>>>>>>>0998>",request.url)
        response = await call_next(request)
        return response
   
app.add_middleware(
    Logging
)

#gzip middleware
app.add_middleware(
    GZipMiddleware,
    minimum_size = 100
)

#global exception handler
@app.exception_handler(Exception)
async def global_unhandled_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An unexpected error occurred. Please try again later. {exc}"},
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
    
    
@app.get("/cause-error")
async def cause_error():
    return 1 / 0  
