# ödev: Matematik, geo, fizik, kimya... derslerinden birini seçerek en sık kullanılan formülleri birer fonksiyona dönüştürünüz.
# Bu işlem bittikten sonra da formulSec()  isimli fonksiyon daha tanımlayıp: kullanıcıya hangi formülle işlem yapmak istediğini sorunuz...
# Gelen cevaba göre o fonksiyonu çalıştırınız
# Tarih : 28.01.2023  Hazırlayan: Ege Kızılkaya

# Matematikte sık kullanılan formüller
import math
def ardisik(n):
    print(f"1'den {n}'e kadar olan sayıların toplamı hesaplanıyor:")
    toplam = (n*(n+1))/2
    return toplam

def ardisikTek(n):
    print(f"1'den {n}'e kadar olan tek sayıların toplamı hesaplanıyor:")
    n = (n + 1) / 2
    toplam = n**2
    return toplam

def ardisikCift(n):
    print(f"2'den {n}'e kadar olan çift sayıların toplamı hesaplanıyor:")
    n /= 2
    toplam = n*(n+1)
    return toplam

def terimSayisi(basla, bit, artis):
    if bit > basla:
        say = ((bit - basla)/artis)+1
    else:
        say = ((basla - bit) / artis) + 1
    return say

def aritmetikOrt():
    sayilar = input("Aritmetik ortalaması hesaplanacak sayıları aralarında ',' olacak biçimde giriniz: ")
    list(sayilar)
    sayilar.split(",")
    for sayi in sayilar:
        sayi = int(sayi)
    ort = (sum(sayilar))/len(sayilar)
    return ort

def mutlak(n):
    if n<0:
        n = -n
    return n

def kareFark(ilkKare, ikinciKare):
    f = math.sqrt(ilkKare)
    q = math.sqrt(ikinciKare)
    acilim = f"({ilkKare}-{ikinciKare})'nin açılımı: ({int(f)}+{int(q)}) x ({int(f)}-{int(q)})'dir."
    return acilim

def islemSec():
    while True:
        islem = input("""Yaygın matematik formülleri kullanan programıma hoşgeldin!
        ardisik = 1'den n'e kadar olan sayıların toplamını bulur.
        ardisikCift = 2'den 2n'e kadar olan çift sayıların toplamını bulur.
        ardisikTek = 1'den 2n-1'e kadar olan tek sayıların toplamını bulur.
        terimSayisi = istenilen değerlere göre bir dizideki terim sayısını hesaplar.
        mutlak = bir sayının mutlak değerini hesaplar.
        kareFark = iki kare farkı özdeşliğini çarpanlarına ayırır.
        q = çıkışı sağlar.
        İşleminizi belirtilen şekillerde yazınız: """)
        if islem == "ardisik":
            sayi = int(input("n. sayıyı giriniz: "))
            toplam = ardisik(sayi)
            print(toplam)
        elif islem == "ardisikCift":
            sayi = int(input("2n. sayıyı giriniz: "))
            toplam = ardisikCift(sayi)
            print(toplam)
        elif islem == "ardisikTek":
            sayi = int(input("2n-1. sayıyı giriniz: "))
            toplam = ardisikTek(sayi)
            print(toplam)
        elif islem == "terimSayisi":
            s1 = int(input("Dizinin başlangıç değerini giriniz: "))
            s2 = int(input("Dizinin bitiş değerini giriniz: "))
            art = int(input("Dizinin düzenli artış değerini giriniz: "))
            say = terimSayisi(s1, s2, art)
            print(say)
        elif islem == "mutlak":
            sayi = int(input("Mutlak değeri alınacak sayıyı giriniz: "))
            n = mutlak(sayi)
            print(n)
        elif islem == "kareFark":
            s1 = int(input("İlk kareyi giriniz: "))
            s2 = int(input("İkinci kareyi giriniz: "))
            acilim = kareFark(s1, s2)
            print(acilim)
        elif islem == "q":
            print("Çıkış sağlanıyor...")
            break
        else:
            print("Hatalı işlem seçiminde bulundunuz. Lütfen kurallara uyarak tekrar deneyin.")

islemSec()
