#!/usr/bin/env python3
"""Run the FFmpeg binary bundled with the project's imageio-ffmpeg package."""
import os
import sys
from imageio_ffmpeg import get_ffmpeg_exe

binary = get_ffmpeg_exe()
os.execv(binary, [binary, *sys.argv[1:]])
