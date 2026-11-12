import sys, wave
from piper import PiperVoice
v=PiperVoice.load(sys.argv[1]); 
with wave.open(sys.argv[3],'wb') as w:
    try:
        from piper import SynthesisConfig
        v.synthesize_wav(sys.argv[2], w, syn_config=SynthesisConfig(length_scale=float(sys.argv[4]) if len(sys.argv)>4 else 1.0))
    except ImportError:
        v.synthesize(sys.argv[2], w)
