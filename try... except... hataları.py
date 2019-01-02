
ilk_sayı = input("İlk sayı: ")
ikinci_sayı = input("İkinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print("Sonuç: ",sayı1/sayı2)
except ValueError:
    print("Sadece sayı girin: ")

##eğer kullanıcı sayı degerli bir veri yerine
##harf degerli bir veri girerse program çöker.
##Dolayısıyla int(ilk_sayı) ve int(ikinci_sayı) kodları,
##kullanıcının girecegi veri türüne göre hata üretme potansiyeline sahiptir.
##O yüzden, burada hata verecegini bildigim o kodları try blogu içine aldım.

ilk_sayı = input("İlk sayı: ")
ikinci_sayı = input("İkinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print("Sonuç: ",sayı1/sayı2)
except ZeroDivisionError:
    print("Bir sayı 0'a bölünmez.")

# expect ZeroDivisionError ile bir sayının 0'a bölünmeyeceği uyarısı verdim.

ilk_sayı = input("İlk sayı: ")
ikinci_sayı = input("İkinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print("Sonuç: ",sayı1/sayı2)
except (ValueError,ZeroDivisionError):
    print("HATA! Bir harf girildi veya bir sayı 0'a bölünmek istendi.")

# YUKARIDAKİ GİBİ YAZDIĞIMDA İKİ HATAYI DA TEK KODDA BELİRTEBİLİRİM.
# İKİ HATAYI TEK BİR KODDA YAZARKEN DİKKAT EDİLMESİ GEREKEN,
# HATALARI except PARANTEZİNE ALMAK VE ARALARINA VİRGÜL KOYMAK.
# VEYA DAHA UZUN YOLU, İKİSİ İÇİN DE print() AÇABİLİRİM.

while True:
    ilk_sayı = input("Programdan 'q' ile çıkabilirsin. Şimdi ilk sayı: ")
    if ilk_sayı == "q":
        break
    ikinci_sayı = input("İkinci sayı: ")
    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print("Sonuç: ",sayı1/sayı2)
    except (ValueError, ZeroDivisionError):
        print("HATA! Bir harf girildi veya bir sayı 0'a bölünmek istendi")
        print("Tekrar dene")

# SADECE HATA AÇIKLAMASI YAZDIRMAK İÇİN:
ilk_sayı = input("İlk Sayı: ")
ikinci_sayı = input("İkinci Sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print("Sonuç :",sayı1,"/",sayı2,"=",sayı1/sayı2)
except ValueError as hata:
   # print(HATA)
# HATA AÇIKLAMASININ YANI SIRA KENDİ AÇIKLAMAM DA GÖRÜNSÜN İSTERSEM EĞER
# SON SATIRDAKİ print(HATA) YERİNE ŞU KODU GİRMEM YETERLİ:
    print("Görünmesini istediğim kendi açıklmam.",hata)
    
# HATA TÜRLERİNİ except (ValueError, ZeroDivisionError): ŞEKLİNDE
# GRUPLANDIRARAK DA YAZABİLİRİM.
ilk_sayı = input("İlk sayı: ")
ikinci_sayı = input("İkinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print("Sonuç: ", sayı1/sayı2)
except (ValueError,ZeroDivisionError) as hata:
    print(hata)
    #VEYA
    print("Kendi mesajım", hata)

# finally... BLOĞU:
try:
    dosya = open("dosyaAdı","r")
    ...burada yapılacak işlemin kodları girilir.
    ...ve birden bir hata oluştu diyelim bu alanda.
except IOError:
    print("Hata mesajı vereceğim yer.")
finally:
    dosya.close()
# finally: İLE PROGRAM ESNASINDA AÇMIŞ OLDUĞUM DOSYAYI HATA OLUŞTUĞU İÇİN AÇIK
# BIRAKMAK ZORUNDA KALMAMIŞ OLDUM. KULLANICI HATAYI DÜZELTTİKTEN SONRA
# ZATEN finally: İLE KAPANMIŞ OLAN DOSYAYI TEKRAR AÇABİLECEK.

# BÜTÜN HATA MESAJLARINI İÇEREN except... :
try:
    ...ilgili kodların yazımı
except:
    print("Kişisel hata mesajı.")
# except...:'İN BU ŞEKİLDE KULLANIMI KULLANICIYA HATANIN NEREDEN GELDİĞİNİ
# GÖSTERMEZ. SADECE HATA VERİR O KADAR. BENİM YAZDIĞIM PROGRAMLARDA DA BUNU
# KULLANIRSAM OLASI BİR HATANIN NEREDEN KAYNAKLANDIĞINI BULAMAYABİLİRİM.
# BU KOD GENELDE ÖNGÖRÜLEMEYEN HATALARIN TANIMINDA KULLANILIR.




















        
