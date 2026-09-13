y1=int(input("1. yazılıyı giriniz..:"))
y2=int(input("2. yazılıyı giriniz..:"))
perf=int(input("perfonmans notunu giriniz..:"))
ortalama=int((y1+y2)/3)
if ortalama>=50:
    print(ortalama,"ile geçti")
else:
    print(ortalama,"ile kaldı")
