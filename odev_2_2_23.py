import time, random

puan = 0

soru_num = [1,2,3,4,5,6,7,8,9,10]
cevaplar = ["a","a","c","b","a","b","b","c","a","a"]
soruldu = []

sorular = [""")Başkentimiz neresidir?
a - Ankara
b - İstanbul
c - Malatya
cevabınızı belirtiniz: """,
""")Dünya'nın en büyük okyanusu hangisidir?
a - Pasifik
b - Hint
c - Atlantik
cevabınızı belirtiniz: """,
""")Python dilinin yapımcısı kimdir?
a - Steve Jobs
b - James Gosling
c - Guido Van Rossum
cevabınızı belirtiniz: """,
""")IntelliJ IDEA ile hangisini programlayamazsınız?
a - kotlin
b - php
c - java
cevabınızı belirtiniz: """,
""")Hangisi web yazımında gerekmedikçe kullanılmayan bir dildir?
a - sql
b - js
c - css
cevabınızı belirtiniz: """,
""")sql için kullanılan en popüler database uygulaması hangisidir?
a - PhpMyAdmin
b - MySQL
c - DataGrip
cevabınızı belirtiniz: """,
""")time modülünde kullanabildiğimiz %m parametresi neden kullanılır?
a - yılı verir (4'lü hane)
b - ayı verir (2'li hane)
c - günü verir (2'li hane)
cevabınızı belirtiniz: """,
""")Unreal Engine hangi dili kullanmaktadır?
a - C#
b - C
c - C++
cevabınızı belirtiniz: """,
""")Unity hangi dili kullanmaktadır?
a - C#
b - C
c - C++
cevabınızı belirtiniz: """,
""")Hangisi swift kodlayabileceğiniz bir uygulamadır?
a - XCode
b - Visual Studio
c - WebStorm
cevabınızı belirtiniz: """]

i = 0
while i < 10:
    r = random.randint(0,9)
    if r in soruldu:
        pass
    else:
        soruldu.append(r)
        
        baslangic_zamani = time.time()
        cevap = input(f"{soru_num[i]}{sorular[r]}")
        gecen_sure = time.time() - baslangic_zamani
        if gecen_sure > 10:
            print("Cevabınız 10 saniye sonrasında verildi! Cevabınız boş kabul edildi...")
        else:
            if cevap.lower() == cevaplar[r]:
                print("Doğru!")
                puan += 10
            else:
                print("Yanlış!")
        i += 1

print(f"Puanınız: {puan}")