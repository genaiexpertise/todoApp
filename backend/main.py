from fastapi import FastAPI, HTTPException,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routers import todos

# initialize the FastAPI app
app = FastAPI()
app.include_router(todos.router)

# CORS configuration 
origins = [
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# global http error handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

# root home page endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Full Stack To Do App!"}

# item endpoint with path parameter
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}, {"message": "Item found"}  # return a dictionary