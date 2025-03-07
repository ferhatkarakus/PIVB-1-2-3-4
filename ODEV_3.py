# Kullanıcıdan sayı al
sayi = int(input("Bir sayı girin: "))

# For döngüsü ile toplam hesaplama
toplam_for = 0
for i in range(1, sayi+1):
    toplam_for += i

print(f"For döngüsü ile 1'den {sayi}'a kadar olan sayıların toplamı: {toplam_for}")

# While döngüsü ile toplam hesaplama
toplam_while = 0
n = 1
while n <= sayi:
    toplam_while += n
    n += 1

print(f"While döngüsü ile 1'den {sayi}'a kadar olan sayıların toplamı: {toplam_while}")
