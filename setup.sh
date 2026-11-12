#!/usr/bin/env bash
# One-time setup for a fresh session. Installs fonts, Python deps, Piper Hindi voice.
set -e
mkdir -p /tmp/fonts && cd /tmp/fonts && [ -d node_modules/@fontsource/inter ] || { npm init -y >/dev/null; npm i -s @fontsource/instrument-serif @fontsource/press-start-2p @fontsource/jetbrains-mono @fontsource/inter @fontsource/caveat >/dev/null; }
pip install -q --break-system-packages playwright piper-tts soundfile numpy 2>/dev/null || true
mkdir -p /tmp/tts && cd /tmp/tts
for v in pratham rohan; do
  [ -f vits-piper-hi_IN-$v-medium/hi_IN-$v-medium.onnx ] || { curl -sSL -o $v.tar.bz2 "https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-hi_IN-$v-medium.tar.bz2" && tar xjf $v.tar.bz2; }
done
which google-chrome >/dev/null && echo "chrome ok" || echo "WARNING: google-chrome missing"
echo "setup done"
