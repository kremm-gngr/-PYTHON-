renkler= ["lacivert","pembe","mavi","sarı","yeşil"]
print(renkler)
renk=input("renk giriniz :")
sayi= renkler.count(renk)
if sayi==0:
    print (renk,sayi,"listede yok.")
else:
    print (renk,sayi,"adet var.")
