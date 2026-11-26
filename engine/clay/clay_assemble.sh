#!/usr/bin/env bash
# usage: clay_assemble.sh WORKDIR SILENT_MP4 [OUT.mp4]   (run in the cloud after the Mac render is staged)
# Doubles 15 fps to 30, burns captions, muxes the mix, H.264 CRF 18. Output is ready for Instagram and YouTube Shorts.
set -euo pipefail
W=$(cd "$1" && pwd); V=$2; OUT=${3:-$W/clay_final.mp4}; cd "$W"
DUR=$(python3 -c "import json;print(json.load(open('anim.json'))['total'])")
ffmpeg -y -v error -i "$V" -i mix_final.wav -vf "fps=30,$(cat caps_filter.txt),format=yuv420p" -map 0:v -map 1:a -t "$DUR" \
  -c:v libx264 -crf 18 -preset veryfast -c:a aac -b:a 192k -movflags +faststart "$OUT.tmp.mp4"
mv "$OUT.tmp.mp4" "$OUT"; ffprobe -v error -show_entries format=duration,size -of csv=p=0 "$OUT"
