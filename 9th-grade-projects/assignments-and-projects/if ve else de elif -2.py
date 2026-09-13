sicaklik=int(input("suyun sıcaklığını giriniz..:"))
if sicaklik>=0:
    print(sicaklik,"derece su sıvıdır.")
elif sicaklik<=-1:
    print(sicaklik,"derece su katıdır.")
elif sicaklik>=100:
    print(sicaklik,"derece su gazdır.")
