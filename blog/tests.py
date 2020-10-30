from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class PostListViewTests(TestCase):
    def test_drafts_hidden(self):
        draft_post = Post.objects.create(
            title="A title", body="Blog content.", slug="test-slug", is_draft=True
        )

        # Test that we start with our post in a draft status
        self.assertTrue(draft_post.is_draft)

        url = reverse("posts")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        # Special Django Helper Method
        self.assertQuerysetEqual(response.context["post_list"], [])

    def test_non_drafts_visible(self):
        post = Post.objects.create(
            title="A title", body="Blog content.", slug="test-slug"
        )

        # Test that we start with our post in a draft status
        self.assertFalse(post.is_draft)

        url = reverse("posts")
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

        # Special Django Helper Method
        self.assertQuerysetEqual(response.context["post_list"], ["<Post: A title>"])

        # Test the webpage content
        self.assertContains(response, "Blog content.")


class PostDetailViewTests(TestCase):
    def test_draft_post_returns_404(self):

        draft_post = Post.objects.create(
            title="A title", body="Blog content.", slug="test-slug", is_draft=True
        )

        url = reverse("post", args=(draft_post.slug,))
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
