from django.core.management.base import BaseCommand, CommandError

from cowepl.models import Music

import pafy

class Command(BaseCommand):
	args = '<youtube_link>'
	help = 'Add music to database'

	def handle(self, *args, **options):
		if len(args) < 1:
			raise CommandError('Link is required')

		try:
			p = pafy.new(args[0])
		except:
			raise CommandError('Failed to obtain video information, please check that you have provided the video id or the full URL containing the video id')

		self.stdout.write('')
		self.stdout.write(str(p))

		audio = p.getbestaudio()

		self.stdout.write('')
		self.stdout.write('Best audio stream: %s ' % str(audio))
		self.stdout.write('')

		music = Music()
		music.title = p.title
		music.video_id = p.videoid
		music.stream_link = audio.url
		music.save()