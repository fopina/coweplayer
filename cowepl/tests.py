from django.test import TestCase

from models import Music

class COWETest(TestCase):

	def test_music_vote(self):
		m = Music()
		m.save()

		self.assertEqual(m.votes, 0)

		m.vote_up()

		self.assertEqual(m.votes, 1)

