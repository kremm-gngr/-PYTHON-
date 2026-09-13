urun1=int(input("1.ürünü giriniz..:"))
urun2=int(input("2.ürünü giriniz..:"))
toplam= urun1 + urun2
if toplam <=200:
    print("ödenecek miktar",toplam,"TL'dir")
else:
    indirim=toplam*0.75
    print("ödenecek miktar",indirim,"TL'dir")
            
