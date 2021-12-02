from Çalıştır import *
import time
depo = Depo()

print("""**********************************************
Şarkıcılar projesine hoşgeldiniz...

İşlemler;

1 - Şarkı ekle

2 - Şarkı sil

3 - Şarkıları Göster

4 - Şarkı Ara

5 - Toplam süreyi gör

Q - Çıkış
**********************************************""")

işlemler = """
İşlemler;

1 - Şarkı ekle

2 - Şarkı sil

3 - Şarkıları Göster

4 - Şarkı Ara

5 - Toplam süreyi gör

Q - Çıkış
"""

while True:
    print(işlemler)
    işlem = input("İşlem seçiniz: ")
    işlem = işlem.upper()
    if işlem == "Q":
        print("Programdan çıkılıyor. Yine bekleriz...")
        break
    elif işlem == "1":
        isim = input("Şarkı adı: ")
        sanatçı = input("Sanatçı: ")
        albüm = input("Şarkı albümü: ")
        şirket = input("Şirket adı: ")
        süre = int(input("Şarkı süresi(Saniye): "))
        şarkı = Şarkı(isim,sanatçı,albüm,şirket,süre)
        print("Şarkı ekleniyor...")
        time.sleep(2)
        depo.şarkı_ekle(şarkı)
        print("Şarkı eklendi.")
    elif işlem == "2":
        isim = input("Silinecek şarkı ismi: ")
        cevap = input("Emin misiniz(E/H): ")
        cevap = cevap.upper()
        if cevap == "E":
            print("Şarkı siliniyor...")
            time.sleep(2)
            depo.şarkı_sil(isim)
            print("Şarkı silindi.")
    elif işlem == "3":
        print(" ")
        depo.şarkılarıgoster()
    elif işlem == "4":
        isim = input("Şarkı ismi: ")
        print("Şarkı aranıyor...")
        time.sleep(2)
        print(" ")
        depo.şarkı_ara(isim)
    elif işlem == "5":
        print("Saniye cinsinden toplam şarkı süresi ölçülüyor...")
        time.sleep(2)
        depo.toplam_şarkı_süresi()
    else:
        print("Geçersiz işlem...")

