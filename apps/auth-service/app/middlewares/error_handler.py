from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import DBError, DBDuplicateError

async def error_handler_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except DBDuplicateError:
        return JSONResponse(status_code=409, content={"detail": "Duplicate entry"})
    except DBError:
        return JSONResponse(status_code=500, content={"detail": "Database error"})
