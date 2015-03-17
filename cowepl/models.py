from django.db import models

class Music(models.Model):
	stream_link = models.CharField(max_length=200)
	video_id = models.CharField(max_length=20)
	title = models.CharField(max_length=50)
	votes = models.IntegerField(default = 0, db_index = True)

	def vote_up(self):
		self.votes += 1
		self.save()

