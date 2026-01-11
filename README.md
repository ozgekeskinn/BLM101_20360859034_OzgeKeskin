# BLM101_20360859034_OzgeKeskin
<h1>Python ile Otomatik HTML Sayfası Oluşturucu</h1>
<h2>Öğrenci Bilgileri</h2> 
  <p>Özge KESKİN</p>
  <p>20360859034</p>
<h2>Proje Konusu</h2> 5. Grup: Ağlar, İnternet ve HTML<br>
<h2>YouTube Linki</h2> https://youtu.be/z4i6LhtKf0A<br>
<h2>Proje Açıklaması</h2>

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

## Kodun Detaylı Çalışma Mantığı

Bu projede Python kullanılarak kullanıcıdan alınan bilgiler işlenmiş ve
bu bilgilerle otomatik olarak bir HTML dosyası üretilmiştir.
Kod; fonksiyonlar, listeler, sözlükler, string işlemleri ve dosya yazma
yapıları kullanılarak modüler şekilde tasarlanmıştır.

---

### Kullanılan Veri Yapıları

- **Liste (list)**  
  ```python
  ogrenci_bilgileri = []
  dersler = []

ogrenci_bilgileri: Öğrenciye ait bilgileri sözlük (dictionary) yapısıyla saklamak için kullanılır.
dersler: Kullanıcının girdiği dersleri tutmak için kullanılır.
**Sözlük (dictionary)**
```python
{
  "adSoyad": adSoyad,
  "bolum": bolum,
  "sinif": sinif,
  "okulNo": okulNo,
  "sehir": sehir
}

Öğrenci bilgileri anahtar–değer (key–value) mantığıyla tutulur.
Bu yapı HTML oluştururken verilere kolay erişim sağlar.

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
