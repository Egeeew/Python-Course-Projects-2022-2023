#  Ödev-1:
# Kullanıcıdan veri alarak bir küpün yüzey alanını ve hacmini hesaplayan program

veri=int(input("Küpün kenarının uzunluğunu birim olarak giriniz: "))
alan=(veri**2)*6
hacim=veri**3
print(f"Bir kenarı {veri} birim olan küpün yüzey alanı: {alan}, hacmi: {hacim}")

#  Ödev-2
# Kullanıcıdan veri alarak dairenin alanını ve çevresini hesaplayan program

import math #pi sayısının tam değerini almak için bu modülü aktardım
r=int(input("Dairenin yarıçapının uzunluğunu birim olarak giriniz: "))
pi=math.pi # math modülünden pi sayısını aldım. Pi sayısını sabitleyedebilirdik. pi=3.14 gibi
alan_d=pi*(r**2)
cevre_d=2*pi*r
print(f"Yarıçapı {r} birim olan dairenin alanı: {alan_d}, çevresi: {cevre_d}")