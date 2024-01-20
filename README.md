# Audio Transcriber

## Overview
Audio Transcriber is a script that utilizes OpenAI's Whisper model to convert audio files into text. This tool is versatile, supporting various audio formats and offering multiple text output options, with Markdown as the default format.

## Prerequisites
- Python 3.11
- Conda for managing environments and dependencies
- Whisper Python environment

## Environment Setup
### Updating Conda
Ensure that Conda is up-to-date:
```bash
conda update conda
```

### Creating and Activating the Python Environment
Create an environment named `whisper_env` using Python 3.11:
```bash
conda create --name whisper_env python=3.11
conda activate whisper_env
```

### Installing OpenAI's Whisper
Install Whisper within the `whisper_env`:
```bash
pip install -U openai-whisper
```

## Installation
Clone or download this repository to your local machine. For example:
```bash
git clone https://github.com/jaredswanson/audio-transcriber.git
cd audio-transcriber
```

## Usage
To use the Audio Transcriber, ensure that the `whisper_env` is activated. Run the script from the directory where it is located:

```bash
python transcriber.py [path_to_audio_file] --format [output_format]
```

### Parameters
- `[path_to_audio_file]`: Specify the path to the audio file.
- `--format [output_format]`: (Optional) Choose the output format (Markdown `md`, plain text `txt`, JSON `json`, CSV `csv`). Defaults to Markdown.

### Example
Transcribe an audio file to Markdown format:
```bash
python transcriber.py /path/to/audio/file.wav --format md
```

## Features
- Supports multiple audio file formats.
- Offers several text output formats.
- Simple and intuitive command-line interface.

## Contributing
Your contributions are welcome! Please feel free to fork the repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvement, don't hesitate to open an issue or contact us.

## License
MIT License

Copyright (c) [year] [your full name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
