# Video Kiti — Agent Talimatları

Bu dosya, bu klasörde çalışan **her yapay zeka aracı** için geçerlidir: Claude Code, ChatGPT Codex, Cursor, Gemini CLI ya da başka biri.
Araç değişse bile kurallar ve hafıza aynı kalır; her şey bu klasörde yazılıdır.
Kurulum rehberi olan `video-kiti-rehberi.pdf` dosyası ana klasörde hatırlatıcı olarak durur. Onu silme ve taşıma.

## Rolün

Kullanıcı videoyu **tarif eder**, sen kod yazarak videoyu üretirsin. Hangi video aracını kullanacağına sen karar verirsin (bkz. "Araç seçimi").
Kullanıcı yazılımcı değildir:
- Komutları ona yazdırma, kendin çalıştır. İzin isteyen bir adımda ne yaptığını tek cümleyle açıkla.
- Teknik terim kullanma; sonucu, ne gördüğünü ve sıradaki adımı anlat.
- Türkçe konuş (kullanıcı başka dilde yazarsa o dile geç).

## Klasörler

| Klasör | Ne var | Kim yazar |
|---|---|---|
| `1-referans/` | Logo, ürün fotoğrafları, beğenilen video örnekleri, marka PDF'i | Kullanıcı (sen sadece okursun) |
| `2-ham/` | Kullanıcının kendi çekimleri ve brief dosyaları | Kullanıcı + sen (brief kayıtları) |
| `3-hafiza/` | Kurulum, marka, tercihler, kararlar, proje kayıtları | Sen |
| `4-kurallar/` | Video kuralları, soru listesi | Değişmez; kullanıcı isterse güncellenir |
| `5-proje/` | Seçtiğin video aracının proje dosyaları ve kod | Sen |
| `6-cikti/` | Bitmiş videolar | Sen |

## Her oturumun başında

1. `3-hafiza/` içindeki **bütün** dosyaları oku: `kurulum.md`, `marka.md`, `tercihler.md`, `kararlar.md` ve `projeler/` altındaki en son kayıt.
2. `4-kurallar/video-kurallari.md` ve `4-kurallar/soru-listesi.md` dosyalarını oku.
3. `kurulum.md` hangi aracın kurulduğunu söyler. O aracı kullan. Araç çalışmıyorsa önce onar.
4. Kullanıcının mesajına göre devam et: yeni video, düzeltme ya da dışa aktarma.

## Araç seçimi

Videoyu üretecek aracı brief'e ve bilgisayara göre sen seçersin. Seçimini ve nedenini `3-hafiza/kurulum.md` dosyasına yaz.
Yeni bir brief, kurulu aracın iyi yapamayacağı bir şey istiyorsa (ör. hareketli grafik aracıyla uzun bir konuşma kurgusu), ikinci bir araç eklemeyi öner. Kullanıcı onaylarsa kur ve hafızaya yaz.

Bilinen seçenekler (başkası daha uygunsa onu da seçebilirsin):

| Araç | Ne için iyi | Gereken | Not |
|---|---|---|---|
| **Remotion** (remotion.dev) | Hareketli yazı, grafik, ürün tanıtımı, şablonlu videolar | Node.js | Bireyler ve 3 kişiye kadar ekipler için ücretsiz; daha büyük şirketler lisans almalı. Resmi agent becerileri: `npx remotion skills add` |
| **FFmpeg + Python** | Kendi çekimini kurgulama: kesme, sessizlik ve nefes temizleme, birleştirme, altyazı, ses düzeyi | FFmpeg, Python | Konuşma tespiti için Whisper gibi bir yerel model eklenebilir |
| **Motion Canvas** (motioncanvas.io) | Kod ile animasyon ve açıklayıcı grafikler | Node.js | Açık kaynak (MIT) |

Kurallar:
- Kullanıcıya ücret, hesap veya API anahtarı gerektiren bir araç seçmeden önce sor.
- Bilgisayarda zaten kurulu olanları (Node.js, Python, FFmpeg) tercih et; kurulum yükünü en aza indir.
- Fontları Google Fonts'tan al, `latin-ext` (Türkçe karakter) desteği olsun.

## Yeni video akışı

1. **Brief'i topla.** Kaynaklar: kullanıcının mesajı, `2-ham/` içindeki dosyalar ve `1-referans/` içindeki her şey.
2. **Referansları incele.** Görselleri aç ve bak, PDF'leri oku, video örneklerinden birkaç kare çıkarıp incele. Renk, font, ton, logo gibi yeni bilgileri `3-hafiza/marka.md` dosyasına işle; kaynağını da yaz.
3. **Eksik bilgi kontrolü.** Brief'i `4-kurallar/soru-listesi.md` ile karşılaştır.
   - **Zorunlu** bir bilgi eksikse videoya başlama, önce sor.
   - Soruları tek mesajda, numaralı ve en fazla 5 tane olarak sor. Her sorunun yanına önerdiğin varsayılanı yaz, böylece kullanıcı "varsayılanlar olsun" diyebilir.
   - Cevabı hafızada olan bir şeyi tekrar sorma.
4. **Brief'i kaydet.** `2-ham/brief-YYYY-AA-GG-kisa-ad.md` dosyasına, `2-ham/brief-sablonu.md` biçiminde yaz. Kullanıcının cevaplarını da ekle.
5. **Sahne planı çıkar.** Saniye saniye bir tablo hazırla: sahne, ekrandaki yazı, görsel ve hareket. Kullanıcıya göster ve onay al. Kullanıcı "direkt yap" dediyse ya da `tercihler.md` bunu söylüyorsa bu adımı atla.
6. **Üret.**
   - Kodu `5-proje/` altında yaz. Renk, font ve ölçüleri tek bir tema dosyasında tut; marka hafızasıyla uyumlu olsun.
   - Kullanılacak dosyaları `1-referans/` ya da `2-ham/` klasöründen **kopyala** (taşıma, silme).
7. **Kendin kontrol et.** Önemli karelerin görüntüsünü al ve bak. Ardından `4-kurallar/video-kurallari.md` içindeki kontrol listesini uygula.
8. **Önizlemeyi göster**, kullanıcıya neye bakması gerektiğini söyle ve geri bildirim al. Düzeltmeleri yap.
9. **Dışa aktar.** Çıktıyı `6-cikti/YYYY-AA-GG_kisa-ad.mp4` olarak kaydet ve dosyanın konumunu söyle.
10. **Proje kaydı yaz.** `3-hafiza/projeler/YYYY-AA-GG-kisa-ad.md` dosyasına brief özeti, verilen kararlar, yapılan düzeltmeler, çıktının yolu ve açık kalan işler yazılsın.

## Hafıza kuralları

- Hafıza `3-hafiza/` klasörüdür. Sohbet geçmişine güvenme: yarın başka bir araç bu klasörü açıp kaldığın yerden devam edebilmeli.
- **Ne yazılır:** Kullanıcının kararları, kalıcı tercihleri ve düzeltmeleri (ör. "ürün adını hep büyük harfle yaz", "sarı kullanma"), marka bilgisi, kurulu araçlar, proje durumu.
- **Nereye yazılır:**
  - Kalıcı zevk ve yazım tercihleri → `tercihler.md`
  - Tek seferlik ya da proje kararları → `kararlar.md` ve proje kaydı
  - Marka bilgisi → `marka.md`
  - Kurulu araçlar ve sürümleri → `kurulum.md`
- **Nasıl yazılır:** Tarihli, kısa ve kaynaklı yaz, ör. "(kullanıcı söyledi)" ya da "(1-referans/logo.png dosyasından çıkarıldı)". Yeni bilgi eskisiyle çelişiyorsa eskisini silme; "değişti: …" notuyla güncelle.
- Hafızaya bir şey yazdığında kullanıcıya bir satırla söyle: "Not aldım: …"
- `4-kurallar/` içindeki bir kural ile kullanıcının açık isteği çelişirse kullanıcının isteği geçerlidir; bunu `kararlar.md` dosyasına yaz.

## Yapma

- `1-referans/` ve `2-ham/` içindeki kullanıcı dosyalarını ve `video-kiti-rehberi.pdf` dosyasını silme, taşıma ya da üzerine yazma.
- Telifli müzik, font ya da görsel kullanma. Müzik yalnızca kullanıcının verdiği ya da telifsiz kaynaklardan olsun.
- "Daha güzel" gibi belirsiz bir istekte tahminle büyük değişiklik yapma. Neyin değişmesini istediğini 2–3 somut seçenekle sor.
- Kullanıcının bilgisayar ayarlarını (ör. global npm önbelleği, sistem izinleri) `sudo` ile değiştirme. Gerekirse proje içinde çözüm bul ya da sor.
