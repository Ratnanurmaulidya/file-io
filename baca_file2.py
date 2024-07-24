#buka file
file_pantun = open("pantun.txt", "r")

# baca isi file 
pantun = (file_pantun.readlines())

# cetak baris nol
print(pantun[0])

# cetak baris pertama
print (pantun[1])

# cetak baris kedua
print(pantun[2])

# cetak baris ketiga
print (pantun[3])

# cetak baris keempat
print (pantun[4])

# tutup file
file_pantun.close()