import pytest


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create_user(username="author", password="pass")
