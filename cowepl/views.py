from django.shortcuts import render, get_object_or_404, redirect

from models import Music

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

def account(request, account_id):
	return redirect('cowepl:index')