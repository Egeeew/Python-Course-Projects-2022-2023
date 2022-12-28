# ödev 1: 1 den 1500 e kadar kaç kere 55 yan yana yazılır?
# ödev 2: while true döngüsü ile istenildiği kadar sayı toplayan ya da sayı çarpan bir program yapınız.
# ödev 3: 250 faktöriyelin içinde 222 sayısı kaç kez tekrar ediyor?
# Tarih : 28.12.2022  Hazırlayan: Ege Kızılkaya

# ödev 1
sayi = []
for i in range(1,1501):
    sayi.append(i)
sayi = str(sayi)
tekrar = sayi.count("55")
print(f"55 sayısı 1 ile 1500 arasında {tekrar} kez tekrar ediyor.")

# ödev 2
secim = int(input("""Hesap Makinesi
1 = Toplama
2 = Çarpma
İşlem Seçimi Yapınız: """))
if secim == 1:
    toplam = 0
    while True:
        sayi = int(input("Toplamak istediğiniz sayı (0 = Çıkış): "))
        toplam += sayi
        if sayi == 0:
            break
        else:
            continue
    print(f"Toplam: {toplam}")
elif secim == 2:
    carpim = 1
    while True:
        sayi = int(input("Çarpmak istediğiniz sayı (1 = Çıkış): "))
        carpim *= sayi
        if sayi == 1:
            break
        else:
            continue
    print(f"Çarpım: {carpim}")
else:
    print("Hatalı girişte bulundunuz.")

# ödev 3
faktor = 1
for i in range(1,251):
    faktor *= i
faktor = str(faktor)
tekrar = faktor.count("222")
print(f"222 sayısı 250! içinde {tekrar} kez tekrar ediyor.")
