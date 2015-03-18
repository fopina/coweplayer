from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from models import Music

import pafy

def index(request):
	return render(
		request,
		'cowepl/index.html',
		{
			'musics': Music.objects.order_by('-votes')
		}
		)

def vote_up(request, music_id):
	music = get_object_or_404(Music, pk=music_id)
	music.vote_up()
	return redirect('cowepl:index')

def add_music(request):
	link = None
	info = None

	if request.POST:
		link = request.POST.get('link')
		if link:
			try:
				info = pafy.new(link)
				if request.POST.get('confirm', '0') == '1':
					music = Music()
					music.title = info.title
					music.video_id = info.videoid
					audio = info.getbestaudio()
					music.stream_link = audio.url
					music.save()
					messages.success(request, '%s added' % info.title)
					return redirect('cowepl:index')
			except:
				messages.error(request, 'Please check that you have provided the video id or the full URL containing the video id')


	return render(
		request,
		'cowepl/add_music.html',
		{
			'link': link,
			'info': info,
		}
		)