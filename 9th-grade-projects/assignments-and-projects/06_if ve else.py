bagajKG=int(input("Bagajınız kaç kg..:"))
if bagajKG<=20:
    print("herhangi bir ücret ödemeyeceksiniz..!")
else:
    ucret=(bagajKG-20)*150
    print("fazladan ödeyeceğiniz",ucret,"TL'dir")
    
