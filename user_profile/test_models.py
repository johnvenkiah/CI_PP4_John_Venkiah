from django.test import TestCase
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime

from .models import Profile


class TestProfileModel(TestCase):
    """
    Detta
    """
    def setUp(self):
        """
        """
        test_user = User.objects.create_user(
            username='test_user', password='test1test', email='test@test.com')
        Profile.objects.create(
            username=test_user,
            slug=slugify(test_user.username),
            created_on=datetime.now().strftime('%H:%M, %d %b %Y%Z'),
            location='46 Courtman Road, London UK'
        )

    def tearDown(self):
        """
        Delete test user, news story and comment
        """
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_profile(self):
        """
        This test tests the news str method and verifies
        """
        user_profile = Profile.objects.get(username='test_user')
        self.assertEqual((user_profile.__str__()), user_profile.username)
