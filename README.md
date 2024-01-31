# Youtube_Downloader
# Main points to understand the code,so lets break down each of them:

## Importing required module:
**from pytube import YouTube**

## Function defination:
**def downloader(url,path):** This function takes two arguments **url**(url of the youtube video) and **path**(where to save the video).

## Creating Youtube Object:
**yt = YouTube(url)**:this line creates a YouTube object passing the url argument to it.

## Filtering Video Streams:
**video_filter = yt.streams.filter(file_extension="mp4")**: Stream is a property of youtube, this line filters the video streams associated with YouTube with file extension "mp4".

## Displaying Available Resolutions:
 The code then iterates over a list of resolutions **(resolutions = ["720p", "480p", "360p"])** and checks if each resolution is available for download.
 Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop.

## User Selection:
**choose = int(input("Enter the option you want to download:"))**: This line prompts the user to enter the option (index) of the resolution they want to download.
 
## Downloading Video:
**video[choose - 1].download(output_path=path)**: This line downloads the selected video stream (video[choose - 1]) to the specified output path (path). It subtracts 1 from the user's choice to match the zero-based index of the video list.
download() is a method of the Stream object that initiates the download process.

## Main Program:
 Oh,you will understand this part yourself.😜😜
