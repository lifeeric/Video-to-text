import sys
import os
import wave
import math
import contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip

print('[SUCCESS] started processing the file')

video_file_name = sys.argv[1]
zoom_video_file_name = video_file_name

file_name = zoom_video_file_name.split('.')
transcribed_audio_file_name = f"{file_name[0]}.wav"

if not os.path.exists(video_file_name):
    print("[ERROR] Video file doesn't exists")
    print("""
        /////////////////////////////////////////////
        please report your error: https://ericgit.me
        /////////////////////////////////////////////

    """)
    sys.exit('[Bye]')

audioclip = AudioFileClip(zoom_video_file_name)
audioclip.write_audiofile(transcribed_audio_file_name)

print(f'[SUCCESS] creating transcript to {file_name[0]}-trans.txt')

with contextlib.closing(wave.open(transcribed_audio_file_name, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)

total_duration = math.ceil(duration / 60)
r = sr.Recognizer()
for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open(f"{file_name[0]}-trans.txt", "a")
    f.write(r.recognize_google(audio))
    f.write(" ")

print('[SUCCESS] Deleting video file')
os.remove(transcribed_audio_file_name)
os.remove(zoom_video_file_name)

f.close()

print("""
//////////////////////////////////////////////////////////////////
                            DONE
//////////////////////////////////////////////////////////////////
            please report your error: https://ericgit.me
""")
print('')
print('')
