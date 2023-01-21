from TextToSpeech.tts import get_length
from pydub import AudioSegment


def add_pause(input_path, output_path, pause):
    input_mp3_file = input_path
    output_mp3_file = output_path

    original_file = AudioSegment.from_mp3(input_mp3_file)
    silenced_file = AudioSegment.silent(duration=pause)
    combined_file = original_file + silenced_file

    combined_file.export(output_mp3_file, format="mp3")