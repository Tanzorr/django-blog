import pytest
from django.db import connection


def test_health_returns_ok_without_database(client):
    # No django_db marker: pytest-django blocks DB access, so this also proves
    # the probe never queries (T-1).
    response = client.get("/health/")

    assert response.status_code == 200
    assert response.content == b"ok"


@pytest.mark.django_db
def test_database_is_reachable():
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        assert cursor.fetchone() == (1,)
