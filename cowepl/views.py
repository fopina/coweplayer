from django.shortcuts import render

from models import Music

def index(request):
	return render(
		request,
		'cowepl/index.html',
		{
			'musics': Music.objects.all()
		}
		)
