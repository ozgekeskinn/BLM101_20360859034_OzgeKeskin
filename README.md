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

<p>ogrenci_bilgileri: Öğrenciye ait bilgileri sözlük (dictionary) yapısıyla saklamak için kullanılır.</p>
<p>dersler: Kullanıcının girdiği dersleri tutmak için kullanılır.</p>
**Sözlük (dictionary)**
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
## input_al() Fonksiyonu
<p>Bu fonksiyon kullanıcıdan öğrenci bilgilerini alır ve hatalı girişleri engeller.</p>
```python
  input()
```
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
