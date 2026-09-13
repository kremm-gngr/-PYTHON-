k1=int(input("1. kenar..:"))
k2=int(input("2. kenar..:"))
k3=int(input("3. kenar..:"))
if k1==k2 and k2==k3:
    print("eşkenar üçgen")
elif k1==k2 or k2==k3 or k1==k3:
    print("ikizkenar üçgen")
else:
    print("çeşit kenar üçgen")
    
