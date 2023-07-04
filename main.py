import os
import yt_dlp
from pathlib import Path

def download_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = input('Enter YouTube URL: ')
    path = input('Select download path (or leave it empty to save to desktop): ')

    if not path:
        desktop_path = str(Path.home() / "Desktop")
        output_path = os.path.join(desktop_path, "YouTube Downloads")
    else:
        output_path = path

    os.makedirs(output_path, exist_ok=True)

    download_audio(url, output_path)
    print('Download complete!')

if __name__ == '__main__':
    main()

