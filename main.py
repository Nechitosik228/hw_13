import uvicorn
from datetime import datetime
from typing import Callable

from fastapi import FastAPI, Request, Response, status

from logg import requests_logger


app = FastAPI()


@app.middleware("http")
async def headers_check(request: Request, call_next: Callable):
    special_header = "x-custom-header"
    resp = await call_next(request)
    headers = dict(resp.headers)
    print(headers)
    if special_header in headers.keys():
        return resp
    else:
        return Response(content="Bad request", status_code=status.HTTP_400_BAD_REQUEST)


@app.middleware("http")
async def logging(request: Request, call_next: Callable):
    time = datetime.now()
    resp = await call_next(request)
    requests_logger.info(
        f"Request Time:{time},Method:{request.method},URL:{request.url},Status Code:{resp.status_code}"
    )
    return resp


@app.get("/")
async def root(resp: Response):
    resp.headers["X-Custom-Header"] = "Hello World"

    return "Hello world"


@app.get("/items")
async def items():
    return {"items": ["foo", "bar"]}


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
