def sayilari_al_ve_bul():
    sayilar = []
    
    for i in range(5):
        sayi = int(input(f"{i+1}. sayıyı girin: "))
        sayilar.append(sayi)
    
    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)
    
    print(f"Girilen sayılar: {sayilar}")
    print(f"En büyük sayı: {en_buyuk}")
    print(f"En küçük sayı: {en_kucuk}")

# Fonksiyonu çağır
sayilari_al_ve_bul()
