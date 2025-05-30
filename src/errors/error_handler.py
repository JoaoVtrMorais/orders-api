from src.main.http_types.http_response import HttpResponse
from .types.http_not_found import HttpNotFoundError
from .types.http_unprocessable_entity import HttpUnprocessableEntityError


def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntityError)):
        # Enviar para um logger
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server error",
                "detail": str(error)
            }]
        }
    )
