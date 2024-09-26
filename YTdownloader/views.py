from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import yt_dlp
videotitle = ""
channelName = ""
videoDescription = ""
channelLink = ""

# function for downloading the youtube video
def download_youtube_video(video_url):
        
    # Configure yt-dlp
    options = {
        'outtmpl':'%(title)s.%(ext)s',
    }
    # Create a YouTube downloader object
    downloader = yt_dlp.YoutubeDL(options)
    
    try:
        # Download the video
        print("Starting download...")
        downloader.download([video_url])
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_video_info(video_url):
    # Configure yt-dlp
    options = {
        'outtmpl':'%(title)s.%(ext)s',
    }
    try:
        # Create a YouTube downloader object
        downloader = yt_dlp.YoutubeDL(options)
        # Extract video information without downloading it
        video_info = downloader.extract_info(video_url, download=False)
        videotitle = video_info.get('title')
        channelName = video_info.get('uploader')
        videoDescription = video_info.get('description')
        channelLink = video_info.get('uploader_url')

        return{
            'title': videotitle,
            'channel': channelName,
            'description': videoDescription,
            'url' : channelLink,
        }
    except Exception as e: 
        raise Exception(f"couldn't get the video details")

# Create your views here.
def home(request):
    return render(request, 'base.html')

def get_url(request):
    if request.method == "POST": 
        url = request.POST.get('url_input')
        if url: 
            try: 
                video_info = get_video_info(url)
                download_youtube_video(url)
                
            except Exception as e: 
                messages.error(request, f'An error occured while processing the url {str(e)}')
    return render(request, 'base.html', {'video_info': video_info})
