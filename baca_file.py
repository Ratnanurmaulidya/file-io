#buka_file
#file_pantun = open("pantun.txt", "r")

#baca isi file
#print (file_pantun.readlines())

#tutup file
#file_pantun.close()# buka file

file_pantun = open("pantun.txt", "r")

# baca isi file
pantun = file_pantun.readlines()

# cetak isi file dengan perulangan
for teks in pantun:
   print (teks)

# tutup file
file_pantun.close()

