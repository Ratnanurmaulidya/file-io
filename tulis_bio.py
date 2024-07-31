print("Selamat Datang di Program Biodata ratna")
print("=================================")

# ambil input dari user 
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

# format teks 
teks = "Nama: {}\nUmur: {}\nAlamat: {}".format(nama, umur, alamat)

# buka file 
buka_file = open("biodata.txt", "a")

# menulis data ke dalam file 
tulis_file = buka_file.write(teks)

# print kalimat validasi bahwa data berhasil ditulis kedalam file 
print("Data berhasil ditambahkan")

# tutup file 
buka_file.close()