from django.test import TestCase

from models import Music

class COWETest(TestCase):

	def test_music_vote(self):
		m = Music()
		m.link = 'https://www.youtube.com/watch?v=Vg1jyL3cr60'
		m.save()

		self.assertEqual(m.votes, 0)

		m.vote_up()

		self.assertEqual(m.votes, 1)

