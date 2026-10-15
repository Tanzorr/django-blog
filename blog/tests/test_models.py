import pytest
from django.db import IntegrityError

from blog.models import Post


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create_user(username="author", password="pass")


def test_str_is_title():
    post = Post(title="Hello")
    assert str(post) == "Hello"


@pytest.mark.django_db
def test_two_posts_cannot_have_same_slug(author):
    Post.objects.create(title="A", slug="same", author=author, body="Text")

    with pytest.raises(IntegrityError):
        Post.objects.create(title="A", slug="same", author=author, body="Text")


@pytest.mark.django_db
def test_published_post_without_date_required(author):
    Post.objects.create(title="A", slug="same", author=author, body="Text")

    with pytest.raises(IntegrityError):
        Post.objects.create(
            title="A", slug="a", author=author, body="Text", status=Post.Status.PUBLISHED
        )


@pytest.mark.django_db
def test_draft_without_date_is_allowed(author):
    Post.objects.create(title="A", slug="a", author=author, body="Text", status=Post.Status.DRAFT)
    assert Post.objects.count() == 1
