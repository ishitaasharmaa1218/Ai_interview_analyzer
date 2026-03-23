import wave
import contextlib
import cv2
import os

video_path = "interview.mp4"
audio_path = "audio.wav"

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video")
    exit()

print("Video loaded successfully")

# Just create placeholder (we will fix method below)
print("NOTE: OpenCV cannot extract audio directly.")