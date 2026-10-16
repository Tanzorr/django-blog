import pytest
from django.urls import reverse
from django.utils import timezone
from pytest_django.asserts import assertContains, assertNotContains

from blog.models import Post


@pytest.fixture
def published_post(author):
    return Post.objects.create(
        title="Hello World",
        slug="hello-world",
        author=author,
        body="Text",
        status=Post.Status.PUBLISHED,
        published_at=timezone.now(),
    )


@pytest.fixture
def draft_post(author):
    return Post.objects.create(
        title="Secret Draft",
        slug="secret-draft",
        author=author,
        body="Text",
        status=Post.Status.DRAFT,
        published_at=timezone.now(),
    )


@pytest.mark.django_db
def test_list_shows_published_post(client, published_post):
    response = client.get(reverse("blog:post_list"))

    assertContains(response, "Hello World")


@pytest.mark.django_db
def test_link_hides_draft(client, draft_post):
    response = client.get(reverse("blog:post_list"))

    assertNotContains(response, "Secret Draft")


@pytest.mark.django_db
def test_detail_shows_published_post(client, published_post):
    response = client.get(reverse("blog:post_detail", kwargs={"slug": "hello-world"}))

    assertContains(response, "Hello World")


@pytest.mark.django_db
def test_draft_detail_returns_404(client, draft_post):
    response = client.get(reverse("blog:post_detail", kwargs={"slug": "secret-draft"}))

    assert response.status_code == 404


@pytest.mark.django_db
def test_unknow_slug_returns_404(client):
    response = client.get(reverse("blog:post_detail", kwargs={"slug": "no-such-post"}))

    assert response.status_code == 404
