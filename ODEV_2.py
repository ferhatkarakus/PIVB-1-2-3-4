#Kullanıcıdan sayı al
sayi = int(input("Bir sayı girin:"))

#Koşullu ifadeler ile negatif pozitif kontrol
if sayi < 0:
    print("Negatif sayı girdiniz!")
elif sayi % 2 == 0:
    print(f"{sayi} bir çift sayıdır.")
else:
    print(f"{sayi} bir tek sayıdır.")

