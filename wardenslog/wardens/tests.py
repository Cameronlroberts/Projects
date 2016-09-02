from django.test import TestCase
from models import Site
from forms import UserLoginForm
from models import models


class SiteTest(TestCase):
        def create_site(self, name='Site test'):
            return Site.objects.create(name=name)

        def test_site_creation(self):
            w = self.create_site()
            self.assertTrue(isinstance(w, Site))
            self.assertEqual(w.__str__(), w.name)

