# Buat file dengan nama Perbandingan_NIM.py
# Nama variabel ditambah 4 digit NIM terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program untuk operator Perbandingan dalam Python

angka1_3025 = int(input("Input angka-1: "))
angka2_3025 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_3025 = angka1_3025 > angka2_3025
print("\nOperator Lebih Besar Dari:")
print("angka1_3025 > angka2_3025:", hasil_3025)

# Lebih kecil dari
hasil_3025 = angka1_3025 < angka2_3025
print("\nOperator Lebih Kecil Dari:")
print("angka1_3025 < angka2_3025:", hasil_3025)

# lebih besar dari atau sama dengan
hasil_3025 = angka1_3025 >= angka2_3025
print("\nOperator Lebih Besar Dari Sama Dengan:")
print("angka1_3025 >= angka2_3025:", hasil_3025)

# lebih kecil dari atau sama dengan
hasil_3025 = angka1_3025 <= angka2_3025
print("\nOperator Lebih Kecil Dari Sama Dengan:")
print("angka1_3025 <= angka2_3025:", hasil_3025)

# Sama dengan
hasil_3025 = angka1_3025 == angka2_3025
print("\nOperator Sama Dengan:")
print("angka1_3025 == angka2_3025:", hasil_3025)

# Tidak sama dengan
hasil_3025 = angka1_3025 != angka2_3025
print("\nOperator Tidak Sama Dengan:")
print("angka1_3025 != angka2_3025:", hasil_3025)

#Tambahan: perbandingan berantai dalam Python
hasil_3025 = 0 < angka1_3025 < 100
print("\nPerbandingan berantai:")
print("0 < angka1_3025 < 100:", hasil_3025)

hasil_3025 = 0 < angka2_3025 < 100
print("0 < angka2_3025 < 100:", hasil_3025)
