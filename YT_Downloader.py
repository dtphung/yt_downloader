from tkinter import *
from tkinter.ttk import Progressbar
from pytube import YouTube
from tkinter.filedialog import askdirectory
import os

# Define the function to download the video
def download_video():
    # Get the video URL from the input field
    video_url = url_entry.get()

    if not video_url.startswith("https://www.youtube.com/watch?v="):
        status_label.config(text="Invalid URL. Please enter a valid YouTube URL.")
        return

    # Create a YouTube object
    try:
        yt = YouTube(video_url, on_progress_callback=show_progress, use_oauth=True, allow_oauth_cache=True)
    except Exception as e:
        status_label.config(text="Error: " + str(e))
        return

    # Select the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    # Get the download directory from the text field
    download_dir = download_dir_entry.get()

    if not download_dir:
        status_label.config(text="Download directory not selected.")
        return

    # Check if the download directory exists
    if not os.path.isdir(download_dir):
        status_label.config(text="Invalid download directory. Please select a valid directory.")
        return

    # Define the file path for the downloaded video
    file_path = download_dir + "/" + yt.title + ".mp4"

    # Download the video to the specified file path
    stream.download(output_path=download_dir, filename=yt.title + ".mp4")

    # Update the status label
    status_label.config(text="Video downloaded successfully!")

# Define a function to show the download progress
def show_progress(stream, chunk, bytes_remaining):
    # Calculate the percent of the file that has been downloaded
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    # Update the progress bar
    progress_bar['value'] = percent
    root.update_idletasks()

# Create the main window
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200") # set the window size to 400x200 pixels

# Create the input field for the video URL
url_label = Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = Entry(root, width=48)
url_entry.pack()

# Create the label and entry field for the download directory
download_dir_frame = Frame(root)
download_dir_frame.pack(side=TOP, pady=10)
download_dir_label = Label(download_dir_frame, text="Download directory:")
download_dir_label.pack(side=TOP)
download_dir_entry = Entry(download_dir_frame, width=40)
download_dir_entry.pack(side=LEFT)
browse_button = Button(download_dir_frame, text="Browse", command=lambda: download_dir_entry.insert(END, askdirectory()))
browse_button.pack(side=LEFT)

# Create the download button
download_button = Button(root, text="Download", command=download_video)
download_button.pack()

# Create the progress bar
progress_bar = Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
progress_bar.pack(pady=10)

# Create the status label
status_label = Label(root, text="")
status_label.pack()

# Start the main loop
root.mainloop()
