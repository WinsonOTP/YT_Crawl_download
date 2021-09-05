from pprint import pprint
import youtube_dl


def get_video_info(youtube_url):
    with youtube_dl.YoutubeDL() as ydl:
        ydl.extract_info(youtube_url, download=True)

Link = input("請輸入影片連結")

if __name__ == '__main__':
    video_info = get_video_info(Link)
    pprint(video_info)

#執行前請先 $ pip install pipenv

#執行方式(在終端機輸入)：pipenv run python YTbug.py