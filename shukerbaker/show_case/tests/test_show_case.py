from django.contrib.auth.models import User
from django.test import TestCase

from show_case.models import ShowCase


class ShowCaseTestCase(TestCase):
    def setUp(self):
        author = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        ShowCase.objects.create(author=author, title='Title1', subtitle='Subtitle1', content='Content1')
        ShowCase.objects.create(author=author, title='Title2', subtitle='Subtitle2', content='Content2')

    def test_show_case(self):
        show_case1 = ShowCase.objects.get(title='Title1')
        show_case2 = ShowCase.objects.get(title='Title2')
        self.assertEqual(show_case1.subtitle, 'Subtitle1')
        self.assertEqual(show_case2.subtitle, 'Subtitle2')
