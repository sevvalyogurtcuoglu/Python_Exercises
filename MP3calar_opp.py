import random

class MP3calar():
    def __init__(self,sarkiListesi=[]):
        self.suanCalanSarki=""
        self.ses=100
        self.sarkiListesi=sarkiListesi
        self.durum=True

    def SarkiSec(self):
        sayac=1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac,sarki))
            sayac+=1

        dinle=int(input("Dinlemek istediğiniz sarkinin numarasını giriniz : "))
        while dinle<1 or dinle>len(self.sarkiListesi):
            dinle=int(input("Dinlemek istediğiniz sarkinin numarasını DOGRU giriniz (1-{}) : ".format(len(self.sarkiListesi))))
        self.suanCalanSarki=self.sarkiListesi[dinle-1]

    def SesArttır(self,arttirmaMiktari=10):
        if self.ses==100:
            pass
        else:
           self.ses+=arttirmaMiktari

    def SesAzalt(self,azaltmaMiktari=10):
        if self.ses==0:
            pass
        else:
            self.ses-=azaltmaMiktari

    def RastgeleSarkiSec(self):
        """a=random.randint(1,len(self.sarkiListesi))
        self.suanCalanSarki=self.sarkiListesi[a-1]"""
        
        if len(self.sarkiListesi)==0:
            print("listeniz boş şarkı ekleyiniz") 
            pass
        else:
            rastgelesarki=random.choice(self.sarkiListesi)
            if rastgelesarki==self.suanCalanSarki:
               rastgelesarki=random.choice(self.sarkiListesi)
               self.suanCalanSarki=rastgelesarki
        

    def SarkiEkle(self):
        sanatci=input("Sanatcı/Grup Giriniz : ")
        sarki=input("sarki adı giriniz : ")
        self.sarkiListesi.append(sanatci + " - " + sarki)

    def SarkiSil(self):
        sayac=1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac,sarki))
            sayac+=1

        sil=int(input("silmek istediğiniz sarkinin numarasını giriniz : "))
        while sil<1 or sil>len(self.sarkiListesi):
            sil=int(input("silmek istediğiniz sarkinin numarasını DOGRU giriniz (1-{}) : ".format(len(self.sarkiListesi))))
        if self.suanCalanSarki==self.sarkiListesi[sil-1]:
            self.suanCalanSarki=""
            
        self.sarkiListesi.pop(sil-1)
    
    def MenuGoster(self):
        print("""
        Şarkı Listesi : {}
        Şuan Çalan Şarkı : {}
        Ses Düzeyi : {}

        ******
        1)Şarkı Sec
        2)Ses Arttır
        3)Ses Azalt
        4)Rastgele Şarkı Sec
        5)Şarkı ekle
        6)Şarkı Sil
        7)Kapat
        """.format(self.sarkiListesi, self.suanCalanSarki, self.ses))


    def Calistir(self):
        self.MenuGoster()
        #secilen=self.Secim()
        secim={1:self.SarkiSec,
               2:self.SesArttır,
               3:self.SesAzalt,
               4:self.RastgeleSarkiSec,
               5:self.SarkiEkle,
               6:self.SarkiSil,
               7:self.Kapat} 

        sec=input("Yapmak İstediğiniz İşlemi Seçiniz : ")
        try:
            sec=int(sec)
            secim[sec]()
        except ValueError:
            print("1 ile 7 arasında bir sayı seçiniz")
            pass
        except KeyError:
            print("1 ile 7 arasında bir sayı seçiniz!!")
            pass  

    def Kapat(self):
        self.durum=False

mp3=MP3calar()
while mp3.durum:
    mp3.Calistir()

print("program sonlandı")
