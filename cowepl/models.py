from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Music(models.Model):
	stream_link = models.CharField(max_length=1000)
	video_id = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	votes = models.IntegerField(default = 0, db_index = True)
	duration = models.IntegerField(default = 0)

	def vote_up(self):
		self.votes += 1
		self.save()

	def generate_link(self):
		return 'https://www.youtube.com/watch?v=%s' % (self.video_id)

	def duration_from_string(self, duration_string):
		try:
			pieces = map(int, duration_string.split(':'))
			self.duration = pieces[0] * 3600 + pieces[1] * 60 + pieces[2]
		except:
			self.duration = 0

	def clean_fields(self, exclude=None):
		if self.duration > settings.COWEPL_MAX_DURATION:
			raise ValidationError('The duration is too long')
		super(Music, self).clean_fields(exclude)


