import time
import random
import logging

from fastapi import Request, status
from starlette.responses import Response
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import BaseHTTPMiddleware


class RequestLogger(BaseHTTPMiddleware):

    def __init__(self, app) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        session_id = random.randint(1000000000, 9999999999)
        logging.info(f"SessionId: {session_id} - Started request in path {request.url.path}")
        logging.info(f"Request Payload: {request.json()}")
        start_time = time.time()

        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000
        formatted_process_time = '{0:2f}'.format(process_time)

        response_body = [section async for section in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))

        logging.info(f"SessionId: {session_id} - Request finished in {formatted_process_time}ms with status code {response.status_code}")
        logging.info(f"Response Payload: {response_body[0].decode()}")

        return response

class ExceptionLogger(BaseHTTPMiddleware):

    def __init__(self, app) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as exception:
            logging.error(f"An exception ocurred during the request processing: {exception}")
            return Response("Internal server error", status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)
