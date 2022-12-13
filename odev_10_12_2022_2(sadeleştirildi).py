# Ödev 10.12.2022.2   -   Koşul Durumu Bulunduran Hesap Makinesi v.2 (sadeleştirilmiş)   -   Ege Kızılkaya

mesaj = """Merhaba, hesap makinesine hoşgeldin.
Yapmak istediğin işlemi aşağıdaki kategorilere göre seçebilirsin!
(Harf büyük/küçüklüğüne dikkat etmek zorunda değilsiniz.)
Toplamak için 'Topla'
Çıkarmak için 'Çıkar'
Çarpmak için 'Çarp'
Bölmek için 'Böl' yazmalısınız.
İşlem girişi yapınız: """

islem = input(mesaj)
islem = islem.upper()

if islem == "TOPLA":
    tekrar = int(input("Kaç sayı toplayacaksınız: "))
    sonuc = 0
    for i in range(1, tekrar + 1):
        sayi = float(input("Sayı giriniz: "))
        sonuc += sayi
    print(f"Sonuç : {sonuc}")

elif islem == "ÇIKAR":
    tekrar = int(input("Kaç sayı çıkaracaksınız: "))
    sonuc = 0
    for i in range(1, tekrar + 1):
        sayi = float(input("Sayı giriniz (Eksilen girilen 1.sayı alınacaktır.): "))
        if i == 1:
            sonuc = sayi
        else:
            sonuc -= sayi
    print(f"Sonuç : {sonuc}")


elif islem == "ÇARP":
    tekrar = int(input("Kaç sayı çarpacaksınız: "))
    sonuc = 1
    for i in range(1, tekrar + 1):
        sayi = float(input("Sayı giriniz: "))
        sonuc *= sayi
    print(f"Sonuç : {sonuc}")

elif islem == "BÖL":
    tekrar = int(input("Kaç sayı böleceksiniz: "))
    sonuc = 1
    for i in range(1, tekrar + 1):
        sayi = float(input("Sayı giriniz (Bölünen girilen 1.Sayı alınacaktır): "))
        if i == 1:
            sonuc = sayi
        else:
            sonuc /= sayi
    print(f"Sonuç : {sonuc}")

else:
    print("Hatalı girişte bulundunuz!")