import time
from fastapi import Request


async def request_timer_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    duration = (time.perf_counter() - start_time) * 1000
    response.headers["X-Process-Time-ms"] = f"{duration:.2f}"
    return response