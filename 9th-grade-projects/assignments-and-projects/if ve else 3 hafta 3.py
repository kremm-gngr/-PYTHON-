boy=float(input("boyunuzu(metre)..:"))
kilo=int (input("Kilonuz..:"))
VKI= kilo/(boy*boy)
if VKI>=18 and VKI<25:
    print(VKI,"-->NORMAL")
elif VKI>=25 and VKI<30:
    print(VKI,"-->KİLOLU")
elif VKI>=30 and VKI<35:
    print(VKI,"-->OBEZ")
elif VKI>=35:
    print(VKI,"-->AŞIRI OBEZ")
