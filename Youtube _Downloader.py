from pytube import YouTube


def downloader(url, path):
    yt = YouTube(url)
    print("Scanning the file......")
    video_filter = yt.streams.filter(file_extension="mp4")

    resolutions = ["720p", "480p", "360p"]

    for i, res in enumerate(resolutions, start=1):
        video = video_filter.filter(res=res)
        if video:
            print(f"{i}. Video Resolution: {res}, size: {video[0].filesize / (1024 * 1024)}MB")
        else:
            print(f"Resolution {res} is not available")

    choose = int(input("Enter the option you want to download:"))

    print("Downloading.....")
    video[choose - 1].download(output_path=path)
    print("Downloaded successfully")


video_url = input("Enter the URL from Youtube:")
char = input('Change the download location? (y or n)')

output = input("Enter the specific location (paste the dir): ") if char.lower() == 'y' else "./"

downloader(video_url, output)
