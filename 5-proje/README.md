# Video Kiti — FFmpeg + Python

Yerel video üretimi için proje içine yalıtılmış Python ortamı kullanılır. FFmpeg, `imageio-ffmpeg` paketinin içinden çağrılır; sistem Python'u veya global ayarlar değiştirilmez.

## Deneme videosu

`5-proje` klasöründeyken:

```sh
.venv/bin/python render_demo.py
```

Varsayılan çıktı `../6-cikti/deneme-videosu.mp4` olur. Farklı konuma yazmak için:

```sh
.venv/bin/python render_demo.py --output ../6-cikti/video-adi.mp4
```

Önizleme için:

```sh
open ../6-cikti/deneme-videosu.mp4
```

FFmpeg komutlarını proje içindeki ikiliyle çalıştırmak için:

```sh
./ffmpeg -version
./ffmpeg -i ../2-ham/girdi.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=0xF7F2E8" -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac ../6-cikti/duzenlenmis.mp4
```

Gerekirse izole Python ortamını kurmak/yenilemek için:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```
