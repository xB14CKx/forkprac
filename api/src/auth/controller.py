from typing import Annotated
from fastapi import APIRouter, Depends, Request
from starlette import status
from ..database.core import get_database_connection
from ..rate_limiting import limiter

router = APIRouter(prefix="/api/v1", tags=["api"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=None)
@limiter.limit("5/minute")
async def get(
    request: Request,
):
    pass
