import os
import argparse
import whisper

def parse_arguments():
    """Parse command line arguments for the audio file path and output format."""
    parser = argparse.ArgumentParser(description='Transcribe audio files using OpenAI Whisper.')
    parser.add_argument('audio_file', type=str, help='Path to the audio file.')
    parser.add_argument('--format', type=str, default='md', choices=['md', 'txt', 'json', 'csv'], help='Output format (default: md for Markdown)')
    return parser.parse_args()

def transcribe_audio(file_path):
    """Transcribe the audio file using Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result['text']

def save_transcription(transcription, file_path, output_format):
    """Save the transcription in the specified format."""
    base_name = os.path.splitext(file_path)[0]
    output_file = f"{base_name}.{output_format}"
    with open(output_file, 'w') as file:
        if output_format == 'md':
            file.write(transcription)
        else:
            # Additional formatting can be added here for other formats
            file.write(transcription)
    print(f"Transcription saved to {output_file}")

def main():
    args = parse_arguments()
    transcription = transcribe_audio(args.audio_file)
    save_transcription(transcription, args.audio_file, args.format)

if __name__ == "__main__":
    main()

