from typing import Optional

from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self, detail: Optional[str] = None):
        if detail is not None:
            self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class RequestHandlingError(BaseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Не удалось обработать запрос"