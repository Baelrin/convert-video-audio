import logging
import moviepy.editor
from pathlib import Path

def get_audio_from_video(video_clip):
 """Get audio from a video clip."""
 try:
   return video_clip.audio
 except Exception as e:
   logging.error(f"An error occurred while getting audio from the video file: {e}")
   return None

def save_audio_as_mp3(video_audio, filename):
 """Save audio as an mp3 file."""
 try:
     video_audio.write_audiofile(filename)
 except Exception as e:
     logging.error(f"An error occurred while writing the audio file: {e}")

def main(video_paths):
 """Main function to extract audio from video files and save them as mp3 files."""
 for video_path in video_paths:
   # Define the path to the video file
   video_file = Path(video_path)

   # Check if the video file exists
   if not video_file.exists():
       logging.error(f"The video file {video_file} does not exist.")
       continue

   try:
       # Create a VideoFileClip object
       video_clip = moviepy.editor.VideoFileClip(str(video_file))
       
       # Get the audio from the video
       video_audio = get_audio_from_video(video_clip)
       
       # Check if audio exists
       if video_audio is not None:
           # Save the audio to a new mp3 file
           mp3_filename = f'{video_file.stem}.mp3'
           if Path(mp3_filename).exists():
               mp3_filename = f'{video_file.stem}_new.mp3'
           save_audio_as_mp3(video_audio, mp3_filename)
       else:
           logging.error("Audio is None")
   except Exception as e:
       logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
 main(['my_video.mp4', 'another_video.mp4'])
