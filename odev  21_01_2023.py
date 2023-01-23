# 21/01/2023 tarihinde verilen ödevler - Ege Kızılkaya
# ödev 1 - ATM negatif işlem engellemek
mevcut = 8500.0 #TL
isim = "Ege"
sifre = 192837
deneme = 0
cikis = 0
islem = """"""

while deneme < 3:
    if cikis == 1:
        break
    sorgu = int(input(f"Hoşgeldiniz {isim}, lütfen devam etmek için şifrenizi giriniz: "))
    if sorgu == sifre:
        while True:
            print(f"""Lütfen yapmak istediğiniz işlemi tuşlayınız,
            Mevcut bakiyeniz: {mevcut}
            0) Çıkış
            1) Para çek
            2) Para yatır
            3) Para gönder
            4) Son işlemleri görüntüle""")
            secim = int(input(">>> "))
            if secim == 1:
                miktarCek = float(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
                if miktarCek <= 0 or miktarCek > mevcut:
                    print("Bu işlemi gerçekleştiremezsiniz. Lütfen tekrar deneyin!")
                else:
                    mevcut -= miktarCek
                    print(f"Hesabınızdan {miktarCek} kadar para çekildi. Yeni mevcut bakiyeniz: {mevcut}")
                    islem += f"\n {miktarCek} TL çekildi."
            elif secim == 2:
                miktarYatir = float(input("Lütfen yatırmak istediğiniz miktarı giriniz: "))
                if miktarYatir <= 0:
                    print("Bu işlemi gerçekleştiremezsiniz. Lütfen tekrar deneyin!")
                else:
                    mevcut += miktarYatir
                    print(f"Hesabınıza {miktarYatir} kadar para yatırıldı. Yeni mevcut bakiyeniz: {mevcut}")
                    islem += f"\n {miktarYatir} TL yatırıldı."
            elif secim == 3:
                kisi = input("Para gönderimi yapacağınız kişinin hesap ismi: ")
                miktarGonder = float(input("Lütfen göndermek istediğiniz miktarı giriniz (Banka gönderim ücreti talep etmeyecektir.): "))
                if miktarGonder <= 0 or miktarGonder > mevcut:
                    print("Bu işlemi gerçekleştiremezsiniz. Lütfen tekrar deneyin!")
                else:
                    mevcut -= miktarGonder
                    print(f"Hesabınızdan {miktarGonder} kadar para {kisi} adlı kişiye gönderildi. Yeni mevcut bakiyeniz: {mevcut}")
                    islem += f"\n {miktarGonder} TL {kisi}'ye gönderildi."
            elif secim == 4:
                print("Hesabınızda gerçekleşen son işlemler: ")
                print(islem)
            elif secim == 0:
                print("İyi günler, çıkış sağlandı.")
                cikis = 1
                break
            else:
                print("Hatalı işlem seçiminde bulundunuz.")
    else:
        deneme += 1
        print(f"Hatalı şifre denemesi. Kalan deneme hakkı: {3 - deneme}")

if deneme >= 3:
    print("3 yanlış şifre denemesinden dolayı hesabınız bloke edilmiştir. Lütfen bankanızla iletişime geçiniz.")

# ödev - 2 10 Soruluk bilgi yarışması
import random as r
msg = ["Python bilgi yarışmasına hoş geldin! \nDevam etmek için ismini gir: ","Yarışma başladı!", "Tebrikler soru doğru!", "Üzgünüm soru yanlış!", "Yarışma sona erdi!", "Skorun çok iyi!", "Skorun iyi!","Skorun ortalamada!","Skorun düşük!","Skorun çok düşük!"]
cvp_ant = [0,2,1,3,4,2,1,0,4,3]
sNum = 1
karsilik = {"A":0,
            "B":1,
            "C":2,
            "D":3,
            "E":4}
soruldu = []
puan = 0
sorular = [""")Ekrana yazı yazdırmaya yarayan komut hangisidir?
A) print
B) printf
C) Console.WriteLine
D) Debug.Log
E) input
""", """)Verilen programa 5 girildiğinde çıkacak sonuç nedir?
    a = 3
    b = 2
    c = input("Bir sayı giriniz": )
    print((a**b)*c)
A) 45
B) 40
C) 555555555
D) 55555555
E) Hata verir
""", """)Pythonda [] işaretleriyle belirtilen değişkenler hangi tiptedir?
A) string
B) list
C) integer
D) dict
E) complex
""", """)Verilen programın çıktısı nedir?
    def islem(x,y):
        print(x**y)
    islem(3,3)
A) 3
B) 9
C) 18
D) 27
E) 36
""", """)Aşağıdakilerden hangisi pythondaki bir kütüphaneyi içeri aktarmaya yarar?
A) lambda
B) opcode
C) pass
D) tuple
E) import
""", """)Hangi karakteri pythonda yorum satırı için kullanırız?
A) /
B) $
C) #
D) &
E) %
""", """)Hangi şıkta koşullu durumlar için kullanılan ifadeler doğru bir şekilde bir arada verilmiştir?
A) switch - case - default
B) if - elif - else
C) if - else if - else
D) if - switch - else
E) switch - else if - default
""", """)Verilen programda eksik bırakılan yere yazılması gereken kod hangisidir?
    a = 15
    b = int(___("Bir sayı giriniz: "))
    a += b
    print(a, b)
A) input
B) print
C) if
D) type
E) str
""", """)Hangisi içine girilen veriyi ondalık sayıya çevirir?
A) int()
B) str()
C) complex()
D) dict()
E) float()
""", """)Programın çıktısı nedir?
    a = "Hoşgeldin"
    b = "ege"
    print(a, b.upper())
A) Hoşgeldin ege
B) hoşgeldin ege
C) Hoşgeldin Ege
D) Hoşgeldin EGE
E) HOŞGELDİN ege
"""]
print(msg[0])
isim = input("")
print(msg[1])
while True:
    sor = r.randint(0,9)
    if sor in soruldu:
        pass
    else:
        soruldu.append(sor)
        cvp = input(f"{str(sNum)}{sorular[sor]} Cevabınızı giriniz: ")
        if karsilik[cvp.upper()] == cvp_ant[sor]:
            puan += 10
            print(msg[2])
        else:
            print(msg[3])
        sNum += 1
    if len(sorular) == len(soruldu):
        break
print(msg[4])
if puan >= 80:
    print(msg[5])
elif puan >= 60:
    print(msg[6])
elif puan >= 50:
    print(msg[7])
elif puan >= 30:
    print(msg[8])
else:
    print(msg[9])