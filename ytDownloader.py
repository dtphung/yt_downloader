from pytube import YouTube

# Replace the video URL with the URL of the video you want to download
 
video_url= input("Pleas enter YouTube URL: ")

# Create a YouTube object
yt = YouTube(video_url,use_oauth=True, allow_oauth_cache=True)

# Select the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Define the file path for the downloaded video
file_path = 'C:\\Users\\Tai\\Downloads'

# Download the video to the specified file path
stream.download(file_path)

print("------------------ done --------------------")