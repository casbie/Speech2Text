# Speech2Text
## Usage
### Streaming recording
```
python streaming_recording.py
```
This code requires library `pyaudio` and `wave`. Once the code start running, say something to record.
The result will be saved as `file.wav`

### Parse audio file
```
python parse_audio.py
```
This code shows the demo of parsing audio file in GCP storage. GCP token is
required, and the resource audio should be saved in Google Storage.

## Note
Google Cloud Platform Speech-to-Text API is involved in the project. Please activate GCP account and generate your json token first
### Reference
https://cloud.google.com/speech-to-text/
