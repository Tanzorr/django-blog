from django.http import HttpRequest, HttpResponse


def health(request: HttpRequest) -> HttpResponse:
    """Liveness probe for the Compose healthcheck.

    Touches no database, so `web` reports healthy before `migrate` has run.
    """
    return HttpResponse("ok", content_type="text/plain")
