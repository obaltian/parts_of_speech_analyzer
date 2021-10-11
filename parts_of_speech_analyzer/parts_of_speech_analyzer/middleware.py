import typing as tp

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpRequest, HttpResponse, HttpResponseServerError


class Process500:

    def __init__(self, get_response: tp.Callable[[HttpRequest], HttpResponse],
                 ) -> None:
        if settings.DEBUG:
            raise MiddlewareNotUsed
        self._get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        return self._get_response(request)

    @staticmethod
    def process_exception(_request: HttpRequest,
                          exception: BaseException,
                          ) -> HttpResponseServerError:
        return HttpResponseServerError(str(exception))
