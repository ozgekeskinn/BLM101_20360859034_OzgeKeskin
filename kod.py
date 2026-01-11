ogrenci_bilgileri = []
dersler = []

def input_al():
    #kullanıcıdan öğrenci bilgilerini almak için oluşturulan fonksiyon burada while döngüsü ile hatalı girişleri engelliyor
    while True:
        #kullanıcıdan input alınırken eğer enter'a basarsa hata vermemesi için ".strip()" eklendi
        adSoyad = input("Adınız ve soyadınız nedir?\n").strip()
        bolum = input("Hangi bölümde okuyorsunuz? \n").strip()
        sinif = input("Hangi sınıftasınız?\n").strip()
        okulNo = input("Okul numaranız nedir?\n").strip()
        sehir = input("Hangi şehirde yaşıyorsunuz?\n").strip()

        # boş giriş kontrolü
        if adSoyad == "" or bolum == "" or sinif == "" or okulNo == "" or sehir == "":
            print("Lütfen tüm bilgileri eksiksiz giriniz.")
            continue
        
        # sayı kontrolü
        if not sinif.isdigit():
            print("Lütfen sınıf bilgisi için geçerli bir sayı giriniz.")
            continue
        sinif = int(sinif) # string to int dönüşümü çünkü input() fonksiyonu string döner

        # okulNo için sayı kontrolü
        if not okulNo.isdigit():
            print("Lütfen okul numarası için geçerli bir sayı giriniz.")
            continue
        okulNo = int(okulNo) # string to int dönüşümü çünkü input() fonksiyonu string döner
        return adSoyad, bolum, sinif, okulNo, sehir

def ders_ekle():
    #kullanıcıdan ders eklemesi için oluşturulan fonksiyon
    devammi= "e"
    while True:
        devammi = input("Ders eklemek istiyor musunuz? (e/h)\n").lower().strip() #kullanıcıdan alınan input'ta boşluk bırakılırsa hata vermemesi için ".strip()" eklendi ve küçük harfe çevirildi
        if devammi=='e':
            ders=input("Hangi dersi alıyorsunuz?\n").strip()
            if ders == "":
                print("Ders adı boş olamaz.")
            else:
                dersler.append(ders) #dersler listesine ekleme yapıldı
        elif devammi=='h':
            print("Tüm derslerinizi eklediniz.")
            break
        else:
            print("Lütfen 'e' veya 'h' giriniz.")
    return dersler

def biyografi_al():
    #kullanıcıdan biyografi almak için oluşturulan fonksiyon
    bio = input("Biyografiniz nedir?\n").strip()
    return bio

def tema_secimi():
    #kullanıcıya tema seçimi sunan fonksiyon
    while True:
        secim = input("Sitenizi hangi tema ile oluşturmak istersiniz? (açık/koyu)\n").lower().strip() #kullanıcıdan alınan input'ta boşluk bırakılırsa hata vermemesi için ".strip()" eklendi ve küçük harfe çevirildi
        if secim  == "acik" or secim == "açık":
            return "#FFFFFF"
        elif secim == "koyu":
            return "#524F4F"
        else:
            print("Lütfen 'açık' veya 'koyu' giriniz.")

def sosyal_medya_ekle():
    secim = input("Github hesabınızı eklemek ister misiniz? (e/h)\n").lower().strip()
    if secim == 'e':
        link = input("Kullanıcı adınız:\n").strip()
        return link
    else:
        return None

def html_olustur(ogrenci_bilgileri, derslerListesi, biyografi, tema, github_link): 
#html dosyasını oluşturmak için fonksiyon
    with open("index.html","w",encoding="utf-8") as file:
        file.write(f"""
        <!DOCTYPE html> 
            <html lang='tr'> 
                <head>  
                <meta charset='UTF-8'> 
                <meta name='viewport' content='width=device-width, initial-scale=1.0'> 
                <title>Öğrenci Bilgileri</title> 
                <style> /* CSS kodları buraya eklendi */
                    body {{font-family:Arial; background-color: {tema};}}
                    .cards{{
                        width:900px; /* Genişlik */
                        margin: 40px auto; /* Ortalamaya yarar */
                        display: flex; /* Elemanları esnek bir düzenle yan yana hizalar ve kolayca konumlandırmayı sağlar */
                        gap:20px; /* Kartlar arasındaki boşluk */
                        align-items: stretch; /* Kartların aynı hizada olmasını sağlar */}}
                    .card{{
                        flex-grow: 1; /* Kartların eşit genişlikte olmasını sağlar */
                        min-width: 250px; /* Kartların çok küçülmesini engeller */
                        border-radius:10px; /* Köşeleri yuvarlar */
                        background-color:#E07272 ;
                        padding:15px; /* İç boşluk */
                        box-shadow: 0 0 5px gray; /* Gölgelendirme efekti */
                        overflow-wrap: break-word; /* Uzun kelimelerin taşmasını engeller */
                    }}
                    h1 {{color: #000000; padding: 10px;}}
                </style> 
                </head>
                <body> 
                <h1 align="center">Öğrenci Bilgileri</h1>
                <div class='cards'>
                        <div class='card'>
                            <h2>Profil</h2>
                            <p><strong>Ad:</strong> {ogrenci_bilgileri[0]['adSoyad']}</p>
                            <p><strong>Bölüm:</strong> {ogrenci_bilgileri[0]['bolum']}</p>
                            <p><strong>Sınıf:</strong> {ogrenci_bilgileri[0]['sinif']}</p>
                            <p><strong>Okul No:</strong> {ogrenci_bilgileri[0]['okulNo']}</p>
                            <p><strong>Şehir:</strong> {ogrenci_bilgileri[0]['sehir']}</p>
                            {github_link}
                        </div>
                        <div class='card'>
                            <h2>Dersler</h2>
                            <ul type='disc'> <!-- yuvarlak madde işaretli liste -->
                                {derslerListesi}
                            </ul>
                        </div>
                        <div class = 'card'>
                            <h2>Biyografi</h2>
                            <p>{biyografi}</p>
                        </div>
                    </div>
                </body> 
            </html>
        """)

def main():
    adSoyad, bolum, sinif, okulNo, sehir = input_al() #öğrenci bilgilerini alır
    ogrenci_bilgileri.append({ #öğrenci bilgilerini sözlük olarak listeye ekler
        "adSoyad": adSoyad,         
        "bolum": bolum,
        "sinif": sinif,
        "okulNo": okulNo,
        "sehir": sehir
    })

    derslerListesi=""
    dersler = ders_ekle() #ders ekleme fonksiyonunu çağırır
    for ders in dersler:
        derslerListesi += f"<li>{ders}</li>\n" #dersleri liste elemanı olarak ekler

    biyografi = biyografi_al() #biyografi alma fonksiyonunu çağırır
    tema = tema_secimi() #tema seçimi fonksiyonunu çağırır
    # main() fonksiyonunda:
    github_link = sosyal_medya_ekle()
    # HTML oluştururken:
    github_html = ""
    if github_link:  # Eğer link varsa
        github_html = f'<p><strong>GitHub:</strong> <a href="https://github.com/{github_link}" target="_blank">@{github_link}</a></p>'

    html_olustur(ogrenci_bilgileri, derslerListesi, biyografi, tema, github_html)  #html oluşturma fonksiyonunu çağırır
    print("Siteniz başarıyla oluşturuldu")
main()