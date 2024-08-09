from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url):
    if 'youtube.com' in url:
        return url.split('v=')[1].split('&')[0]
    elif 'youtu.be' in url:
        return url.split('/')[-1]
    else:
        raise ValueError("Invalid YouTube URL")


def get_text(video_id):
    data = YouTubeTranscriptApi.get_transcript(video_id)
    text = ""

    for i in data:
        text += i['text']

    return text