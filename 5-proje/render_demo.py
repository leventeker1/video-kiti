#!/usr/bin/env python3
"""Create the Video Kit's 15-second, 1080x1920 installation demo."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import Tuple

from PIL import Image, ImageDraw, ImageFont
from imageio_ffmpeg import get_ffmpeg_exe

WIDTH, HEIGHT, FPS = 1080, 1920, 30
DURATION = 15
TOTAL_FRAMES = FPS * DURATION
CREAM = (247, 242, 232)
INK = (40, 39, 36)
ORANGE = (229, 99, 49)
MUTED = (126, 118, 106)
FONT_FILE = Path(__file__).resolve().parent / "assets" / "NotoSans[wdth,wght].ttf"


def font(size: int, weight: int = 700) -> ImageFont.FreeTypeFont:
    face = ImageFont.truetype(str(FONT_FILE), size=size)
    # Noto Sans is a variable font with [wdth, wght] axes.
    try:
        face.set_variation_by_axes([weight, 100])
    except (AttributeError, OSError, ValueError):
        pass
    return face


def mix(a: Tuple[int, int, int], b: Tuple[int, int, int], amount: float) -> Tuple[int, int, int]:
    amount = max(0.0, min(1.0, amount))
    return tuple(round(x + (y - x) * amount) for x, y in zip(a, b))


def ease_out(value: float) -> float:
    value = max(0.0, min(1.0, value))
    return 1 - (1 - value) ** 3


def centered_text(draw: ImageDraw.ImageDraw, text: str, y: int, face: ImageFont.FreeTypeFont,
                  color: Tuple[int, int, int], spacing: int = 18, align: str = "center") -> None:
    box = draw.multiline_textbbox((0, 0), text, font=face, spacing=spacing, align=align)
    text_w, text_h = box[2] - box[0], box[3] - box[1]
    x = (WIDTH - text_w) / 2 - box[0]
    top = y - text_h / 2 - box[1]
    draw.multiline_text((round(x), round(top)), text, font=face, fill=color,
                        spacing=spacing, align=align)


def make_background() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), CREAM)
    draw = ImageDraw.Draw(image)
    # A restrained frame and abstract orange shapes; all meaningful text stays inside
    # the vertical-video safe area (y=220..1500).
    draw.rounded_rectangle((42, 42, WIDTH - 42, HEIGHT - 42), radius=38,
                           outline=(225, 216, 201), width=2)
    draw.ellipse((WIDTH - 266, 222, WIDTH - 156, 332), fill=ORANGE)
    draw.ellipse((95, HEIGHT - 312, 175, HEIGHT - 232), fill=(239, 220, 193))
    draw.rounded_rectangle((94, 402, 250, 416), radius=7, fill=ORANGE)
    draw.line((94, HEIGHT - 408, WIDTH - 94, HEIGHT - 408), fill=(225, 216, 201), width=2)
    return image


BACKGROUND = make_background()
FONT_SMALL = font(30, 600)
FONT_MEDIUM = font(42, 600)
FONT_HERO = font(106, 750)
FONT_CATEGORY = font(150, 750)
FONT_CLOSE = font(82, 750)


def draw_header(draw: ImageDraw.ImageDraw, label: str, frame_index: int) -> None:
    draw.text((96, 300), label, font=FONT_SMALL, fill=MUTED)
    # Four short bars show the demo's progress without adding extra copy.
    base_x, base_y, bar_w, gap = 96, 1506, 185, 18
    active = min(3, max(0, (frame_index - 120) // 54)) if frame_index >= 120 else 0
    for index in range(4):
        color = ORANGE if index <= active else (225, 216, 201)
        draw.rounded_rectangle((base_x + index * (bar_w + gap), base_y,
                                base_x + index * (bar_w + gap) + bar_w, base_y + 10),
                               radius=5, fill=color)


def render_frame(frame_index: int) -> Image.Image:
    t = frame_index / FPS
    frame = BACKGROUND.copy()
    draw = ImageDraw.Draw(frame)

    if t < 4:
        label = "FİKİR  /  VİDEO KİTİ"
        draw_header(draw, label, frame_index)
        progress = ease_out(t / 0.55)
        color = mix(CREAM, INK, progress)
        y = 905 + round((1 - progress) * 28)
        centered_text(draw, "Bir içerik\nfikrim var.", y, FONT_HERO, color, spacing=14)
        accent_width = round(132 * progress)
        draw.rounded_rectangle((WIDTH // 2 - accent_width // 2, 1172,
                                WIDTH // 2 + accent_width // 2, 1186), radius=7, fill=ORANGE)
        draw.text((96, 1450), "01  /  03", font=FONT_MEDIUM, fill=MUTED)
        return frame

    if t < 11.2:
        index = min(3, int((t - 4) / 1.8))
        labels = ["Trendler", "UGC", "Video", "AI"]
        slot_start = 4 + index * 1.8
        local_t = t - slot_start
        progress = ease_out(local_t / 0.26)
        color = mix(CREAM, INK, progress)
        draw_header(draw, "FİKİRDEN ÜRETİME", frame_index)
        draw.text((96, 758), f"0{index + 1}  /  04", font=FONT_MEDIUM,
                  fill=mix(CREAM, MUTED, progress))
        y = 966 + round((1 - progress) * 24)
        centered_text(draw, labels[index], y, FONT_CATEGORY, color)
        # Short orange underline grows into place with the title.
        length = round((90 + 34 * len(labels[index])) * progress)
        draw.rounded_rectangle((WIDTH // 2 - length // 2, 1100,
                                WIDTH // 2 + length // 2, 1114), radius=7, fill=ORANGE)
        draw.text((96, 1450), "02  /  03", font=FONT_MEDIUM, fill=MUTED)
        return frame

    progress = ease_out((t - 11.2) / 0.45)
    draw_header(draw, "İÇERİK ÜRETENLERİN LABORATUVARI", frame_index)
    color = mix(CREAM, INK, progress)
    y = 930 + round((1 - progress) * 26)
    centered_text(draw, "İçerik üretenlerin\nlaboratuvarı", y, FONT_CLOSE, color, spacing=18)
    draw.rounded_rectangle((96, 1450, 96 + round(132 * progress), 1464), radius=7, fill=ORANGE)
    draw.text((264, 1434), "03  /  03", font=FONT_MEDIUM, fill=MUTED)
    return frame


def render(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = get_ffmpeg_exe()
    command = [
        ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS), "-i", "pipe:0",
        "-an", "-frames:v", str(TOTAL_FRAMES), "-c:v", "libx264",
        "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", "-metadata", "title=Video Kiti — Deneme",
        str(output),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    assert process.stdin is not None
    try:
        for frame_index in range(TOTAL_FRAMES):
            process.stdin.write(render_frame(frame_index).tobytes())
        process.stdin.close()
    except BrokenPipeError:
        process.stdin.close()
    stderr = process.stderr.read().decode("utf-8", errors="replace") if process.stderr else ""
    return_code = process.wait()
    if return_code != 0:
        raise RuntimeError(f"FFmpeg render failed ({return_code}): {stderr}")
    print(f"Created: {output}")
    print(f"Format: H.264 MP4, {WIDTH}x{HEIGHT}, {FPS} fps, {DURATION} seconds")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "6-cikti" / "deneme-videosu.mp4",
                        help="MP4 destination (default: ../6-cikti/deneme-videosu.mp4)")
    args = parser.parse_args()
    render(args.output.expanduser().resolve())


if __name__ == "__main__":
    main()
