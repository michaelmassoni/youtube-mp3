from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format':'bestaudio'})

while True:
    try:
        print('YouTube Downloader'.center(40, '_'))
        URL = input('Enter URL: ')
        audio_downloader.extract_info(URL)
    except Exception:
        print("Failed to download audio. Try again.")