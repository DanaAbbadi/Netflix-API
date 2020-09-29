from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Netflix
# Create your tests here.

class NetflixTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='password')
        test_user.save()

        test_post = Netflix.objects.create(
            user = test_user,
            series = 'Suits',
            movie = 'Not a movie.',
            episode = '13',
            season = '3',

        )
        test_post.save() # Save the object to mock Database

    def test_netflix_content(self):
        netflix = Netflix.objects.get(id=1)
        actual_user = str(netflix.user)
        actual_series = str(netflix.series)
        actual_movie = str(netflix.movie)
        actual_episode = str(netflix.episode)
        actual_season = str(netflix.season)

        self.assertEqual(actual_user, 'test_user')
        self.assertEqual(actual_series, 'Suits')
        self.assertEqual(actual_movie, 'Not a movie.')
        self.assertEqual(actual_episode, '13')
        self.assertEqual(actual_season, '3')

    def test_api_permissions(self):
        response = self.client.get(reverse('netflix'))
        self.assertEqual(response.status_code, 200)

        # Has permission to view data
        self.assertContains(response, 'Suits')

        response2 = self.client.get(reverse('netflix_details', args='1'))
        self.assertEqual(response2.status_code, 200)
        # self.assertContains(response2, 'Post')

        response_update = self.client.post(reverse('netflix_details', args='1'), {
            'series': 'friends',
        })
        # self.assertContains(response_update, 'friends')
        # It will fail because user didn't sign in, so he can't update
        self.assertEqual(response_update.status_code, 405)




