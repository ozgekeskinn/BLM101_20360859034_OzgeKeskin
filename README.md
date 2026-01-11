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

- <b>Liste (list)</b>
  ```python
  ogrenci_bilgileri = []
  dersler = []

<p>ogrenci_bilgileri: Öğrenciye ait bilgileri sözlük (dictionary) yapısıyla saklamak için kullanılır.</p>
<p>dersler: Kullanıcının girdiği dersleri tutmak için kullanılır.</p>
-** Sözlük (dictionary)**
```python
{
  "adSoyad": adSoyad,
  "bolum": bolum,
  "sinif": sinif,
  "okulNo": okulNo,
  "sehir": sehir
}
``` 
<p>Öğrenci bilgileri anahtar–değer (key–value) mantığıyla tutulur.</p>
<p>Bu yapı HTML oluştururken verilere kolay erişim sağlar.</p>

## Kullanıcıdan Veri Alma ve Kontroller
### input_al() Fonksiyonu
<p>Bu fonksiyon kullanıcıdan öğrenci bilgilerini alır ve hatalı girişleri engeller.</p>
```python 
input()

<p>Kullanıcıdan veri almak için kullanılır. Python’da her input varsayılan olarak string döner.</p>
```python
strip()
```
-Boş giriş kontrolü
```python
if adSoyad == "":
```
<p>Kullanıcının boş veri girmesi engellenir.</p>
```python
isdigit()
```
<p>Girilen değerin sadece rakamlardan oluşup oluşmadığını kontrol eder.</p>
- int() dönüşümü
```python
sinif = int(sinif)
```
<p>Sayısal işlemler için string veri integer tipe dönüştürülür.</p>

### Ders ekleme : ders_ekle() Fonksiyonu
<p>Bu fonksiyon kullanıcıdan birden fazla ders alabilmek için while döngüsü kullanır.</p>

lower()
<p>Büyük–küçük harf farkını ortadan kaldırır (E, e, H, h gibi).</p>

append()
dersler.append(ders)
<p>Girilen dersleri dersler listesine ekler.</p>

### Tema Seçimi : tema_secimi() Fonksiyonu
<p>Kullanıcının seçimine göre arka plan rengi belirler.</p>
<p>Açık tema → #FFFFFF</p>
<p>Koyu tema → #524F4F</p>
<p>Tema rengi HTML içinde CSS arka plan rengi olarak kullanılır.</p>

### GitHub Ekleme : sosyal_medya_ekle() Fonksiyonu
<p>Kullanıcı isterse GitHub kullanıcı adı alır.</p>
<p>Eğer kullanıcı eklemek istemezse None döner.</p>
<p>HTML oluşturulurken bu kontrol edilir ve sadece varsa link eklenir.</p>

### HTML Dosyası Oluşturma : html_olustur() Fonksiyonu
<p>Bu fonksiyon programın en önemli kısmıdır.</p>

open()
open("index.html", "w", encoding="utf-8")

<p>"w": Dosya yazma modudur.</p>
<p>utf-8: Türkçe karakter sorunlarını önler.</p>

file.write()
<p>HTML ve CSS kodları string olarak dosyaya yazılır.</p>

f"{ogrenci_bilgileri[0]['adSoyad']}"
<p>Python değişkenlerinin HTML içine dinamik olarak yerleştirilmesini sağlar.</p>

<p><b>HTML ve CSS Yapısı</b></p>
<p>HTML içinde:</p>
<div class="card"> 
  yapısı ile kart tasarımı oluşturulmuştur.
<ul><li> 
  etiketleriyle ders listesi gösterilmiştir.

<p>CSS ile:</p>
<p>flex yapısı kullanılarak kartlar yan yana hizalanmıştır.</p>
<p>border-radius, box-shadow ile görsel düzen sağlanmıştır.</p>

## Program Akışı
### main() Fonksiyonu
<p>Programın çalışmasını başlatan ana fonksiyondur.</p>
<p>Kullanıcıdan öğrenci bilgileri alınır.</p>
<p>Dersler liste hâlinde toplanır.</p>
<p>Biyografi ve tema seçimi yapılır.</p>
<p>GitHub linki isteğe bağlı eklenir.</p>
<p>HTML dosyası oluşturulur.</p>
<p>Program tamamlanır.</p>

## Sonuç
Program çalıştırıldığında kullanıcıdan alınan bilgilerle otomatik olarak başlıklı, listeli ve stillendirilmiş bir statik HTML web sayfası oluşturulur. Bu proje, Python’da dosya yazma, string işleme, liste–sözlük kullanımı ve temel web sayfası üretimini öğretmeyi amaçlamaktadır.

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
