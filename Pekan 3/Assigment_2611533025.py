# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_3025 = int(input("Input angka-1: "))
angka2_3025 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3025)
print("Nilai awal angka2 =", angka2_3025)

# Assigment biasa
hasil_3025 = angka1_3025
print("\nHasil assigment biasa (=)")
print("Hasil =", hasil_3025)

# Assigment penambahan
hasil_3025 = angka1_3025 
hasil_3025 += angka2_3025
print("\nAssigment penambahan (+=)")
print("Hasil =", hasil_3025)

# Assigment pengurangan
hasil_3025 = angka1_3025
hasil_3025 -= angka2_3025
print("\nAssigment pengurangan (-=)")
print("Hasil =", hasil_3025)

# Assigment perkalian
hasil_3025 = angka1_3025
hasil_3025 *= angka2_3025
print("\nAssigment perkalian (*=)")
print("Hasil =", hasil_3025)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_3025 != 0:
    hasil_3025 = angka1_3025
    hasil_3025 /= angka2_3025
    print("\nAssigment pembagian (/=)")
    print("Hasil =", hasil_3025)
    # Operator tambahan
    hasil_3025 = angka1_3025
    hasil_3025 //= angka2_3025
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =", hasil_3025)

    hasil_3025 = angka1_3025
    hasil_3025 %= angka2_3025
    print("\nAssigment sisa bagi (%=)")
    print("Hasil =", hasil_3025)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_3025 = angka1_3025
hasil_3025 **= angka2_3025
print("\nAssigment perpangkatan (**=)")
print("Hasil =", hasil_3025)