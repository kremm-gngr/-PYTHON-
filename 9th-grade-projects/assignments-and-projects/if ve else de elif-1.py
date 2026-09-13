sayi=int(input("0-999 arası bir sayı giriniz..: "))
if sayi<0 or sayi>999:
    print ("aralık dışı sayı girdiniz..!")
else:
    if sayi>-1 and sayi<10:
        print(sayi,"1 basamaklıdır.")
    elif sayi>=10 and sayi<=99:
        print(sayi,"2 basamaklıdır.")
    elif sayi>=100 and sayi<=999:
        print(sayi,"3 basamaklıdır.")
    
         
