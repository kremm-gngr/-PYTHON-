ad= input("Adınızı Girin:")
maas= float (input("Maaşınızı giriniz:"))
yil=int(input("çalışma yılınız:"))
if yil>0 and yil<=5:
    print("Zamlı maşınız-->",maas*1.1)
elif yil>=6 and yil<=10:
    print("Zamlı maaşınız-->",maas*1.15)
elif yil>10:
    print("Zamlı maaşınız-->",maas*1.25)
            
