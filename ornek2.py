print (" Hesap Makinesi (1)Toplama (2)Çıkarma (3)Çaprma (4)Bölme")


veri=input("işlem:")

if veri=="1":
    x=int(input("ilk sayı:"))
    x=float(x)
    y=int(input("ikinci sayı:"))
    y=float(y)
    print("sonuç:", x+y)

elif veri=="2":
    x=int(input("ilk sayı:"))
    x=float(x)
    y=int(input("ikinci sayı:"))
    y=float(y)
    print("sonuç:",x-y)

elif veri=="3":
    x=int(input("ilk sayı:"))
    x=float(x)
    y=int(input("ikinci sayı:"))
    y=float(y)
    print("sonuç:",x*y)

elif veri=="4":
    x=int(input("ilk sayı:"))
    x=float(x)
    y=int(input("ikinci sayı:"))
    y=float(y)
    print("sonuç:",x/y)

else:
    print("yanlış seçim:(program kapanıyor...")
    quit()
