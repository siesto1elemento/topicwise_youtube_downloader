from django.shortcuts import render
from pytube import YouTube

def download_view(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        try:
            yt = YouTube(video_url)
            video = yt.streams.get_highest_resolution()
            video.download()
            context = {'message': 'Download complete!'}
        except Exception as e:
            context = {'message': f'Error: {str(e)}'}
    else:
        context = {}
    return render(request, 'downloader/download.html', context)