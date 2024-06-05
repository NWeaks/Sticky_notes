# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Note, Post

class NoteModelTests(TestCase):
    def test_note_creation(self):
        note = Note.objects.create(title='Test Note', content='This is a test note.')
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.content, 'This is a test note.')

class PostModelTests(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')

class NoteViewsTests(TestCase):
    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_detail_view(self):
        note = Note.objects.create(title='Test Note', content='This is a test note.')
        response = self.client.get(reverse('note_detail', args=(note.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_detail.html')

    def test_note_create_view(self):
        response = self.client.get(reverse('note_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_form.html')

    def test_note_edit_view(self):
        note = Note.objects.create(title='Test Note', content='This is a test note.')
        response = self.client.get(reverse('note_edit', args=(note.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_form.html')

    def test_note_delete_view(self):
        note = Note.objects.create(title='Test Note', content='This is a test note.')
        response = self.client.get(reverse('note_delete', args=(note.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_confirm_delete.html')

class PostViewsTests(TestCase):
    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/post_list.html')

    def test_post_detail_view(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.')
        response = self.client.get(reverse('post_detail', args=(post.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/post_detail.html')

    def test_post_create_view(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/post_form.html')

    def test_post_edit_view(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.')
        response = self.client.get(reverse('post_edit', args=(post.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/post_form.html')

    def test_post_delete_view(self):
        post = Post.objects.create(title='Test Post', content='This is a test post.')
        response = self.client.get(reverse('post_delete', args=(post.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/post_confirm_delete.html')
