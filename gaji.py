GajiPokok        = float(input("Masukkan gaji pokok karyawan           : "))
Uangtransport    = float(input("Masukkan uang transport harian         : "))
Uangmakan        = float(input("Masukkan uang makan harian             : "))
Tunjanganjabatan = float(input("Masukkan uang tunjangan jabatan        : "))
Honorlembur      = float(input("Masukkan uang honor lembur             : "))
Totalbekerja     = float(input("Masukan total bekerja selama satubulan :"))

Total_Gaji = (GajiPokok + (Uangtransport*Totalbekerja) + (Uangmakan*Totalbekerja) + Tunjanganjabatan + Honorlembur)

print("Total gaji karyawan adalah :",Total_Gaji )