
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import sys
from mutagen.mp3 import MP3
import config
import random

def creat_session():
    my_config = config.load_config()
    session = Session(aws_access_key_id=my_config['AmazonAWSCredential']['aws_access_key_id'],
                      aws_secret_access_key=my_config['AmazonAWSCredential']['aws_secret_access_key'],
                      region_name=my_config['AmazonAWSCredential']['region_name']
                      )
    return session
def create_tts(text, path):
    my_config = config.load_config()
    session = creat_session()
    polly = session.client("polly")

    try:
        voice_id = my_config['TextToSpeechSetup']['voice_id']
        if my_config['TextToSpeechSetup']['multiple_voices']:
            voices = ["Joanna", "Justin", "Kendra", "Matthew"]
            voice_id = random.choice(voices)

        response = polly.synthesize_speech(Text=text,
                                           OutputFormat="mp3",
                                           VoiceId=voice_id)
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
               output = path
               try:
                # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                       file.write(stream.read())

               except IOError as error:
                  # Could not write to file, exit gracefully
                  print(error)
                  sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

def get_length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None