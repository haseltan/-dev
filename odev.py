print("     Bu program bir basketbol oyuncusuna ilişkin girdiğiniz bilgileri işleyip yeni bilgiler üretir.")
print("")

print("     Oyuncunun girdiği toplam maç sayısını, başarılı ve başarısız serbest, ikilik, üçlük atış sayısını ")
print("girdikten sonra program atış çeşitlerindeki başarı oranlarını, toplam atış sayısını ve maç başına ortalama")
print("ortalama başarılı atış sayısını yazdıracak")
print("")

oyuncu_adi = input("Oyuncunun adını giriniz :")
mac_sayisi = int(input("Oyuncunun oynadığı maç sayısını giriniz :"))

basarili_serbest = int(input("Oyuncunun başarılı serbest atış sayısını giriniz :"))
basarisiz_serbest = int(input("Oyuncunun başarısız serbest atış sayısını giriniz :"))

basarili_ikilik = int(input("Oyuncunun başarılı ikilik atış sayısını giriniz :"))
basarisiz_ikilik = int(input("Oyuncunun başarısız ikilik atış sayısını giriniz :"))

basarili_ucluk = int(input("Oyuncunun başarılı üçlük atış sayısını giriniz :"))
basarisiz_ucluk = int(input("Oyuncunun başarısız üçlük atış sayısını giriniz :"))

serbest_toplam = basarili_serbest + basarisiz_serbest
serbest_basari_orani = round(basarili_serbest / (serbest_toplam / 100))

ikilik_toplam = basarili_ikilik + basarisiz_ikilik
ikilik_basari_orani = round(basarisiz_ikilik / (ikilik_toplam / 100))

ucluk_toplam = basarili_ucluk + basarisiz_ucluk
ucluk_basari_orani = round(basarili_ucluk / (ucluk_toplam / 100))

toplam_sayi = basarili_serbest * 1 + basarisiz_ikilik * 2 + basarili_ucluk * 3
mac_basina_ortalama_sayi = round(toplam_sayi / mac_sayisi)

print("Oyuncu adı : ", oyuncu_adi)
print("Oyuncunun oynadığı maç sayisi : {0} maç.".format(mac_sayisi))

print("Oyuncunun serbest atışlardaki başarı oranı : %{0} başarı oranı.".format(serbest_basari_orani))
print("Oyuncunun ikilik atışlardaki başarı oranı : %{0} başarı oranı.".format(ikilik_basari_orani))
print("Oyuncunun üçlük atışlardaki başarı oranı : %{0} başarı oranı.".format(ucluk_basari_orani))

print("Oyuncunun attığı toplam sayı : {0} sayı.".format(toplam_sayi))
print("Oyuncunun maç başına attığı ortalama sayı : {0} sayı.".format(mac_basina_ortalama_sayi))