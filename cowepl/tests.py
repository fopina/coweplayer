from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from models import Music

class COWETest(TestCase):

	def test_music_vote(self):
		m = Music()
		m.save()

		self.assertEqual(m.votes, 0)

		m.vote_up()

		self.assertEqual(m.votes, 1)

class COWEViewTest(TestCase):

	def setUp(self):
		self.c = Client()

	def test_music_add_bad_link(self):
		res = self.c.post(reverse('cowepl:add'), {
			'link': 'https://www.youtube.com/',
			})
		self.assertContains(
			res,
			'Please check that you have provided the video id or the full URL containing the video id',
			status_code = 200
			)

	def test_music_add(self):
		res = self.c.post(reverse('cowepl:add'), {
			'link': 'https://www.youtube.com/watch?v=XFkzRNyygfk',
			})
		self.assertEqual(res.status_code, 200)
		self.assertIn('info', res.context)
		self.assertEqual(res.context['info'].videoid, 'XFkzRNyygfk')
		self.assertEqual(res.context['info'].title, 'Radiohead - Creep')

		# nothing should have been saved at this point
		self.assertEqual(Music.objects.count(), 0)

		res = self.c.post(reverse('cowepl:add'), {
			'link': 'https://www.youtube.com/watch?v=XFkzRNyygfk',
			'confirm': '1',
			})
		self.assertEqual(res.status_code, 302)
		self.assertEqual(Music.objects.count(), 1)

		m = Music.objects.get(pk=1)
		self.assertEqual(m.video_id, 'XFkzRNyygfk')
		self.assertEqual(m.title, 'Radiohead - Creep')

	def test_music_add_too_long(self):
		res = self.c.post(reverse('cowepl:add'), {
			'link': 'https://www.youtube.com/watch?v=om8invGWkeo',
			})
		self.assertEqual(res.status_code, 200)
		self.assertIn('info', res.context)
		self.assertEqual(res.context['info'].videoid, 'om8invGWkeo')
		self.assertEqual(res.context['info'].title, 'The Best Of - Radiohead (Full Album)')

		# nothing should have been saved at this point
		self.assertEqual(Music.objects.count(), 0)

		res = self.c.post(reverse('cowepl:add'), {
			'link': 'https://www.youtube.com/watch?v=om8invGWkeo',
			'confirm': '1',
			})
		self.assertContains(
			res,
			'The duration is too long',
			status_code = 200
			)

		self.assertEqual(Music.objects.count(), 0)