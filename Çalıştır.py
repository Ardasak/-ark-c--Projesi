import sqlite3

class Şarkı():
    def __init__(self,isim,sanatçı,albüm,şirket,süre):
        self.isim = isim
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.şirket = şirket
        self.süre = süre
    def __str__(self):
        return "Şarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nŞirket: {}\nSüre: {}".format(self.isim, self.sanatçı, self.albüm,self.şirket, self.süre)
    
class Depo:
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Şarkıcılar.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create Table If not exists şarkılar (isim TEXT, sanatçı TEXT, albüm TEXT, şirket TEXT, süre INT)")
        self.baglanti.commit()
    def baglanti_kes(self):
        self.baglanti.close()
    def şarkı_ekle(self,şarkı):
        self.cursor.execute("Insert into şarkılar Values(?,?,?,?,?)",(şarkı.isim,şarkı.sanatçı,şarkı.albüm,şarkı.şirket,şarkı.süre))
        self.baglanti.commit()
    def şarkı_sil(self,isim):
        self.cursor.execute("Delete From şarkılar where isim = ?",(isim,))
        self.baglanti.commit()

    def toplam_şarkı_süresi(self):
        self.cursor.execute("Select * From şarkılar")
        liste = self.cursor.fetchall()
        toplamsüre = 0
        for i in liste:
            for a in i:

                süre = i[4]
                süre1 = int(süre)
            toplamsüre+=süre1
        print(toplamsüre)


    def şarkı_ara(self,isim):
        self.cursor.execute("Select * From şarkılar where isim=?",(isim,))
        liste = self.cursor.fetchall()
        if(len(liste)==0):
            print("O isimde şarkı bulunamadı.")
        else:
            şarkı = Şarkı(liste[0][0],liste[0][1],liste[0][2],liste[0][3],liste[0][4])
            print(şarkı)
            print("")
    def şarkılarıgoster(self):
        
        self.cursor.execute("Select * From şarkılar")
        liste = self.cursor.fetchall()
        if (len(liste) == 0):
            print("Hiç şarkı yok.")
        else:
            for i in liste:
                şarkı = Şarkı(i[0], i[1], i[2], i[3], i[4])
                print(şarkı)
                print("")
