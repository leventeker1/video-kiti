# Video Kiti

Bu depo, yerel video düzenleme ve üretim kiti için yönergeleri, kaynak dosyaları ve kuralları içerir.

## Kurulum

macOS'ta proje kökünden:

```sh
cd 5-proje
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Deneme videosu

```sh
cd 5-proje
.venv/bin/python render_demo.py
```

Video `6-cikti/deneme-videosu.mp4` konumuna kaydedilir. FFmpeg komutları `5-proje/ffmpeg` ile çalıştırılır.

## İçerik

- `AGENTS.md`: bu klasörde çalışacak araçlara yönelik iş akışı.
- `5-proje/`: Python ve FFmpeg kaynakları.
- `1-referans/`, `2-ham/`: kullanıcı malzemeleri ve brief'ler için yerel klasörler.
- `3-hafiza/`: kurulum ve kullanıcı tercihleri.
- `4-kurallar/`: video kalite ve brief kuralları.

`.gitignore`, sanal ortamı, kullanıcının yerel referans/çekim dosyalarını ve üretilmiş videoları depodan hariç tutar.
