# Kurulum Kaydı

> Agent ilk kurulumda doldurur, araç eklendikçe günceller.

- **Kurulum tarihi:** 2026-11-22
- **Kurulumu yapan araç:** ChatGPT Codex (Codex masaüstü)
- **İşletim sistemi:** macOS 27.0.1, Apple Silicon (ARM64)
- **Kullanıcının ağırlıklı video türü:** İkisi de: kendi çekimlerini kurgulama ve hareketli yazı/grafik (kurulum sorusuna yanıt)
- **Seçilen video aracı / araçları ve nedeni:** FFmpeg + Python — kullanıcı ücretli lisans gerektirmeyen yolu seçti; bu ikili çekim kurgusunu ve Python ile yazı/grafik üretimini destekler.
- **Kurulan yazılımlar ve sürümleri:** Python 3.9.6 (mevcut); proje içindeki `.venv` ortamında Pillow 11.0.0 ve FFmpeg 7.1 içeren `imageio-ffmpeg` 0.6.0. Noto Sans değişken TTF, `latin-ext` desteğiyle `5-proje/assets/` içinde.
- **Deneme videosu:** `6-cikti/deneme-videosu.mp4` (H.264 MP4, 15 saniye, 1080×1920, 30 fps; kareler ve Türkçe metin görsel olarak kontrol edildi)
- **Karşılaşılan sorunlar ve çözümleri:** npm, Homebrew ve sistem FFmpeg bulunmadı; sistem ayarları değiştirilmeden FFmpeg proje içindeki Python ortamına kuruldu. Marka dosyaları henüz klasöre eklenmediği için `marka.md` boş şablon bırakıldı.
- **Önizleme ve dışa aktarma nasıl yapılır:** `cd "5-proje" && .venv/bin/python render_demo.py --output ../6-cikti/video-adi.mp4`; önizleme: `open ../6-cikti/video-adi.mp4`; FFmpeg: `5-proje/ffmpeg` komutu.
