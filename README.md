# BLM101_20360859034_OzgeKeskin
Python ile Otomatik HTML Sayfası Oluşturucu
Öğrenci Bilgileri: 
  Özge KESKİN
  20360859034
Proje Konusu: 5. Grup: Ağlar, İnternet ve HTML
YouTube Linki: https://youtu.be/z4i6LhtKf0A
Proje Açıklaması: Kodun ne yaptığı, nasıl çalıştırılacağı (kurulum gerekip gerekmediği) ve kodun
çalışma mantığının detaylı açıklaması (Markdown formatında).

## Proje Açıklaması
Bu proje, Python programlama dili kullanılarak kullanıcıdan alınan bilgileri temel alan
statik bir HTML web sayfası oluşturan bir uygulamadır.  
Program, Python’un **string işlemleri** ve **dosya yazma (file write)** yeteneklerini kullanarak
dinamik olarak `index.html` dosyası üretir.

Oluşturulan HTML sayfası; öğrenci bilgileri, alınan dersler ve biyografi bölümlerini içeren,
basit CSS ile stillendirilmiş kart yapısına sahiptir.

---

## Program Ne Yapar?
- Kullanıcıdan **öğrenci bilgilerini** (ad-soyad, bölüm, sınıf, okul numarası, şehir) alır.
- Kullanıcının aldığı **dersleri liste hâlinde** toplar.
- Kullanıcıdan **biyografi** bilgisi alır.
- Kullanıcıya **açık veya koyu tema** seçimi sunar.
- İsteğe bağlı olarak **GitHub profili** eklenmesini sağlar.
- Tüm bu bilgileri kullanarak otomatik olarak bir **index.html** dosyası oluşturur.
- HTML dosyası açıldığında, girilen bilgilere göre düzenlenmiş bir web sayfası görüntülenir.

## Nasıl Çalıştırılır?
Bu proje için **ekstra kurulum veya kütüphane gerekmez**.

### Gereksinimler
- Python 3.x

### Çalıştırma Adımları
1. Python dosyasını bilgisayarınıza indirin.
2. Terminal veya komut satırında dosyanın bulunduğu dizine gidin.
3. Aşağıdaki komutu çalıştırın:
   ```bash
   python kod.py
