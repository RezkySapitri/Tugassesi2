Totaluangbelanja = float(input("Masukan total uang belanja anda :"))
TotalBelanja     = float(input("Masukan total belanja anda      :"))

#tambahkan diskon untuk pembelian diatas 70.000 ribu
if TotalBelanja > 70000:
    diskon = 0.1 * TotalBelanja
    TotalBelanjaSetelahDiskon = TotalBelanja - diskon
    kembalian = Totaluangbelanja - TotalBelanjaSetelahDiskon

print ("Uang kembalian anda :%.0f"% kembalian)

