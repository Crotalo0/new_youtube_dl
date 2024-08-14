# YouTube Downloader

This is a simple YouTube downloader application built using Python and Tkinter. It allows users to download audio or video from YouTube and merge them if both are selected.

## Features

- **Download Options**: Choose to download either audio only or both audio and video.
- **Merge Functionality**: Automatically merges the downloaded audio and video into a single file. 
- **Custom Save Location**: Users can choose where to save the downloaded files.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
- **pytube**: This is a lightweight library to download videos from the web.
- **tkinter**: This is the standard Python interface to the Tk GUI toolkit.
- **MoviePy**: A library used for merging video and audio.

To run, first create a virtual environment:
1. open PowerShell
2. Create the environment: ```python -m venv venv```
3. Activate it: ```venv\Scripts\Activate.ps1```
4. Install requirements: ``` python -m pip install -r requirements.txt```
5. Finally run the app: ```python app.py``` 

## How to Use

- Enter YouTube URL: Copy and paste the URL of the YouTube video you want to download.
- Select Download Option:
    - Only Audio: Download just the audio of the video.
    - Audio and Video: Download both the video and audio, and merge them into a single file.
- Select Save Path: Choose the directory where you want to save the downloaded files.
- Start Download: Click the "Download" button. The application will show progress pop-ups as it downloads and processes the files.
- At the end in the selected folder, will be created an Audio folder that will contain the audio trace of the video, a Video folder with only the video trace without audio and the *_merged.mp4
