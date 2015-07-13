from django.core.management.base import BaseCommand, CommandError

from cowepl.models import Music

import time

class Command(BaseCommand):
	help = 'Pool database for musics to play'

	def handle(self, *args, **options):
		while True:
			ms = Music.objects.order_by('-votes')

			if ms.count() < 1:
				self.stdout.write('No musics found')
				self.stdout.write('Retry in 10secs...')
				time.sleep(10)
				continue

			m = ms[0]
			m.votes = 0
			m.save()

			self.stdout.write('Playing %s' % m.title)
			self.stdout.write('Waiting %d seconds' % m.duration)
			time.sleep(m.duration)