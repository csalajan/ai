#!/bin/bash
#arecord -d 4 -f cd -t wav file.wav > /dev/null 2>&1
rec -c 1 -r 22050 file.wav silence 1 0 15% 1 00:00:02 15% 

sox file.wav file.flac rate 16k

wget -q -U "Mozilla/5.0" --post-file file.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v1/recognize?lang=en-us&client=chromium" | cut -d\" -f12 >stt.txt

rm file.wav file.flac
