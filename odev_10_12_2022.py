# Ödev 10.12.2022   -   Koşul Durumu Bulunduran Hesap Makinesi v.1   -   Ege Kızılkaya

mesaj = """
Merhaba, hesap makinesine hoşgeldin.
Yapmak istediğin işlemi aşağıdaki kategorilere göre seçebilirsin!
(Harf büyük/küçüklüğüne dikkat etmek zorunda değilsiniz.)
Toplamak için 'Topla'
Çıkarmak için 'Çıkar'
Çarpmak için 'Çarp'
Bölmek için 'Böl'
Hesap makinesinden çıkış için 'Çıkış'  yazmalısınız.
İşlem girişi yapınız: 
"""

while True:
    islem = input(mesaj)
    islem = islem.lower()

    if islem == "topla":
        print("Toplama işlemini seçtiniz.")
        toplam = 0
        while True:
            sayi = input("Toplanacak sayıyı giriniz, işlemi sonlandırmak için 'q': ")
            if sayi == "q":
                break
            else:
                try:
                    sayi = float(sayi)
                    toplam += sayi
                except ValueError:
                    print("Desteklenmeyen veri girişinde bulundunuz.")
        print(f"Girdiğiniz sayıların toplamı: {toplam}")

    elif islem == "çıkar":
        print("Çıkarma işlemini seçtiniz.")
        fark = 0
        dongu = 0
        while True:
            sayi = input("Çıkarılacak sayıyı giriniz, işlemi sonlandırmak için 'q' (Eksilen sayı default olarak ilk değer alınır): ")
            if sayi == "q":
                break
            else:
                try:
                    dongu += 1
                    if dongu == 1:
                        sayi = float(sayi)
                        fark = sayi
                    else:
                        sayi = float(sayi)
                        fark -= sayi
                except ValueError:
                    print("Desteklenmeyen veri girişinde bulundunuz.")
        print(f"Girdiğiniz sayıların farkı: {fark}")

    elif islem == "çarp":
        print("Çarpma işlemini seçtiniz.")
        carpim = 1
        while True:
            sayi = input("Çarpılacak sayıyı giriniz, işlemi sonlandırmak için 'q': ")
            if sayi == "q":
                break
            else:
                try:
                    sayi = float(sayi)
                    carpim *= sayi
                except ValueError:
                    print("Desteklenmeyen veri girişinde bulundunuz.")
        print(f"Girdiğiniz sayıların çarpımı: {carpim}")

    elif islem == "böl":
        print("Çıkarma işlemini seçtiniz.")
        bolum = 0
        dongu = 0
        while True:
            sayi = input("Bölecek sayıyı giriniz, işlemi sonlandırmak için 'q' (Bölünen sayı default olarak ilk değer alınır): ")
            if sayi == "q":
                break
            else:
                try:
                    dongu += 1
                    if dongu == 1:
                        sayi = float(sayi)
                        bolum = sayi
                    else:
                        sayi = float(sayi)
                        bolum /= sayi
                except ValueError:
                    print("Desteklenmeyen veri girişinde bulundunuz.")
        print(f"Girdiğiniz sayıların bölümü: {bolum}")
    elif islem == "çıkış":
        print("Çıkış sağlanıyor...")
        break

    else:
        print("Yanlış seçimde bulundunuz.")