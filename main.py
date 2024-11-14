import uvicorn
from typing import Annotated
from fastapi import FastAPI, Header
from custom import CustomMidlleware

app = FastAPI()

app.add_middleware(CustomMidlleware, path=["/", "/items"])


@app.get("/")
async def root(custom_header: Annotated[str | None, Header()]):
    return {"custom header": custom_header}


@app.get("/items")
async def root():
    return {"items": "items"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)

