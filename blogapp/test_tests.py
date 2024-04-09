from django.test import TestCase, Client
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class ModelTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='12345')
        self.test_post = Post.objects.create(title='Test Post', content='Test content', author=self.test_user)
        self.test_comment = Comment.objects.create(post=self.test_post, author=self.test_user, text='Test comment')

    def test_post_model(self):
        self.assertEqual(self.test_post.title, 'Test Post')
        self.assertEqual(self.test_post.content, 'Test content')
        self.assertEqual(self.test_post.author, self.test_user)

    def test_comment_model(self):
        self.assertEqual(self.test_comment.text, 'Test comment')
        self.assertEqual(self.test_comment.author, self.test_user)

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create_user(username='testuser', password='12345')
        self.test_post = Post.objects.create(title='Test Post', content='Test content', author=self.test_user)

    def test_post_list_api_view(self):
        # Authenticate the client
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)

    def test_post_create_api_view(self):
        # Authenticate the client
        self.client.force_authenticate(user=self.test_user)
        response = self.client.post(reverse('post-list'), {'title': 'New Post', 'content': 'New content'})
        self.assertEqual(response.status_code, 201)