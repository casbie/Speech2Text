import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# Loads the audio into memory

uri = 'gs://speech2text_nlp/N2_tango_15.wav'
audio = types.RecognitionAudio(uri=uri)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='ja-JP',
)

# Detects speech in the audio file

operation = client.long_running_recognize(config, audio)
response = operation.result(timeout=90)

# print the result
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u'{}'.format(result.alternatives[0].transcript))