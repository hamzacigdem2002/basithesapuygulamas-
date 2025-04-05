def topla (a,b):
    return a + b

def cikar (a,b):
    return a - b

def carp (a,b):
    return a * b

def bolme (a,b):
    if b != 0:
        return a / b
    else:
        return "Sıfıra bölme hatası !"

def kare_al(a):
    return a ** 2    
    
print("hesap makinasına hoşgeldiniz !".title())   
islem = input("Yapmak istediğiniz işlemi seçiniz (+,-,*,/,**,e): ")

if islem == "e":
    print("Hesap makinasından çıkılıyor...")
elif islem == "**":
    karesayi = float(input("Karesini almak istediğiniz sayıyı girin : "))
    print(f"Sonuç: {kare_al(karesayi)}")
else:
    sayi1 = float(input("Birinci sayıyı girin : "))
    sayi2 = float(input("İkinci sayıyı girin : "))

    if islem == "+":
        print(f"Sonuç: {topla(sayi1,sayi2)}")
    elif islem == "-":
        print(f"Sonuç: {cikar(sayi1,sayi2)}")
    elif islem == "*":
        print(f"Sonuç: {carp(sayi1,sayi2)}")  
    elif islem == "/":
        print(f"Sonuç: {bolme(sayi1,sayi2)}")
    else:
        print("Geçersiz İşlem !")

print("İyi günler !")