#!/usr/bin/env bash
# One-time setup for a fresh session. Installs fonts, Python deps, Piper Hindi voice.
set -e
mkdir -p /tmp/fonts && cd /tmp/fonts && [ -d node_modules/@fontsource/playfair-display ] || { npm init -y >/dev/null; npm i -s @fontsource/instrument-serif @fontsource/press-start-2p @fontsource/jetbrains-mono @fontsource/inter @fontsource/caveat @fontsource/playfair-display @fontsource/noto-sans-devanagari >/dev/null; }
pip install -q --break-system-packages playwright piper-tts soundfile numpy 2>/dev/null || true
mkdir -p /tmp/tts && cd /tmp/tts
for v in pratham rohan; do
  [ -f vits-piper-hi_IN-$v-medium/hi_IN-$v-medium.onnx ] || { curl -sSL -o $v.tar.bz2 "https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-hi_IN-$v-medium.tar.bz2" && tar xjf $v.tar.bz2; }
done
if ! which google-chrome >/dev/null; then
  echo "google-chrome missing: installing Playwright Chromium"; python3 -m playwright install --with-deps chromium >/dev/null 2>&1 || python3 -m playwright install chromium
  CH=$(ls -d ~/.cache/ms-playwright/chromium-*/chrome-linux*/chrome 2>/dev/null | head -1); [ -n "$CH" ] && { mkdir -p ~/.local/bin; ln -sf "$CH" /usr/bin/google-chrome 2>/dev/null || ln -sf "$CH" ~/.local/bin/google-chrome; }
fi
which ffmpeg >/dev/null || { apt-get install -y -qq ffmpeg >/dev/null 2>&1 || pip install -q --break-system-packages imageio-ffmpeg; }
# self-check: every tool the pipeline needs
python3 -c "import playwright, numpy, soundfile, piper" && echo "python deps ok" || echo "ERROR: python deps missing"
# Kokoro natural Hindi voices (hm_psi, hm_omega)
pip install -q --break-system-packages kokoro-onnx 2>/dev/null || true
mkdir -p /tmp/tts/kx && for f in kokoro-v1.0.onnx voices-v1.0.bin; do [ -f /tmp/tts/kx/$f ] || curl -sSL -o /tmp/tts/kx/$f https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f; done
python3 -c "import kokoro_onnx" && echo "kokoro ok" || echo "ERROR: kokoro missing (fallback: Piper voices)"
which google-chrome >/dev/null && echo "chrome ok" || echo "ERROR: no chrome"
which ffmpeg >/dev/null && echo "ffmpeg ok" || echo "ERROR: no ffmpeg"
ls /tmp/tts/vits-piper-hi_IN-rohan-medium/*.onnx >/dev/null && echo "voice ok" || echo "ERROR: voice missing"
echo "setup done"
