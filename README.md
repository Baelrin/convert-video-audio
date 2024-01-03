# Video to Audio Converter

This Python script extracts audio from video files and saves them as mp3 files. It uses the `moviepy` library to handle video and audio processing.

## Features

- Extracts audio from video files.
- Saves extracted audio as mp3 files.
- Handles exceptions during the extraction and saving processes.

## Usage

To run the script, provide a list of video paths as arguments. The script will extract the audio from each video file and save it as an mp3 file.

Example:

```bash
python main.py ['my_video.mp4', 'another_video.mp4']
```

This command will extract the audio from `my_video.mp4` and `another_video.mp4`, and save them as `my_video.mp3` and `another_video.mp3` respectively.

## Installation

Ensure you have Python 3 and the `moviepy` library installed on your system. You can install `moviepy` using pip:

```bash
pip install moviepy
```

## License

This project is licensed under the terms of the MIT license.

## Contact

For any questions or issues, feel free to reach out to the maintainer.

---
