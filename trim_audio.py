# trim_audio.py - workflow & script to download all videos from shore-stein-papier on youtube as audio & get rid of intro & outro

# step 1: download videos from playlist as audio using yt-dlp package for terminaö (installed via homebrew): https://github.com/ytdl-org/youtube-dl
    # yt-dlp -o '%(playlist)s/%(playlist_index)s %(title)s.%(ext)s' 'https://www.youtube.com/playlist?list=PLpr-NGsAGodEbDePSO3wivni39lgdLQjW' -f m4a

# step 2: use python script below to cut start & end of audios in directory

import os
import subprocess
from pydub.utils import mediainfo

# Define input and output directories
input_directory = "/Users/Name/Downloads/Shore, Stein, Papier"
output_directory = "/Users/Name/Downloads/Shore, Stein, Papier cutted"

# Create the output directory if it does not exist
os.makedirs(output_directory, exist_ok=True)

# Loop through all audio files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".flac") or filename.endswith(".m4a") or filename.endswith(".webm"):  # Add more extensions as needed
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(output_directory, filename)

        # Get the duration of the input file in seconds
        info = mediainfo(input_file)
        duration = float(info['duration'])
        
        # Calculate the end time (duration - 22 seconds)
        end_time = duration - 22
        
        # Construct the FFmpeg command
        ffmpeg_command = [
            "ffmpeg",
            "-i", input_file,
            "-ss", "5",
            "-to", str(end_time),
            "-c", "copy",
            output_file
        ]
        
        # Run the FFmpeg command
        subprocess.run(ffmpeg_command)
