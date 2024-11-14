from typing import Awaitable, Callable
from datetime import datetime
from fastapi import Request, Response, status
from starlette.middleware.base import BaseHTTPMiddleware
from logg import requests_logger

class CustomMidlleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: BaseHTTPMiddleware,
        path
    ):
        self.path=[x for x in path]
        super().__init__(app)

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        if request.scope.get("path") in self.path:
            if not request.headers.get("custom-header"):
                return Response(content="Bad request",status_code=status.HTTP_400_BAD_REQUEST)
        time=datetime.now()
        response = await call_next(request)
        requests_logger.info(
        f"Request Time:{time},Method:{request.method},URL:{request.url},Status Code:{response.status_code}"
        )
        return response