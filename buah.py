jeruk   = 3
apel    = 2
mangga  = 0
manggis = 5
durian  = 2

harga_jeruk = 15_000
harga_apel  = 30_000
harga_mangga = 20_000
harga_manggis = 7_000
harga_durian = 50_000

total_jeruk = jeruk*harga_jeruk
total_apel = apel*harga_apel
total_mangga = mangga*harga_mangga
total_manggis = manggis*harga_manggis
total_durian = durian*harga_durian

total_belanja = (total_jeruk+total_apel+total_mangga+total_manggis+total_durian)

print ("Total yang harus anda bayar adalah :") 
print (f"{jeruk} kilo jeruk   = {total_jeruk:1,.0f} rupiah")
print (f"{apel} kilo apel    = {total_apel:1,.0f} rupiah")
print (f"{mangga} kilo mangga  = {total_mangga:1,.0f} rupiah")
print (f"{manggis} kilo manggis = {total_manggis:1,.0f} rupiah")
print (f"{durian} kilo durian  = {total_durian:1,.0f} rupiah")
print (f"total keseluruhan belanja anda = {total_belanja:1,.0f} rupiah")

