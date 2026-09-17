# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("======================================")
print("1. OPERATOR KEANGGOTAAN")
print("======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3025 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3025 = [int(angka.strip()) for angka in input_data_3025.split(',')]

nilai_dicari_3025 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3025 = nilai_dicari_3025 in data_3025
print("\nOperator keanggotaan IN")
print(nilai_dicari_3025,"in",data_3025,"=",hasil_3025)

# Operator not in
hasil_3025 = nilai_dicari_3025 not in data_3025
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3025,"not in",data_3025,"=",hasil_3025)

print("======================================")
print("2. OPERATOR IDENTIAS")
print("======================================")

# objek1 menggunakan list dari input perngguna
object1_3025 = data_3025

# objek2 merujuk pada objek yang sama dengan objek1
object2_3025 = object1_3025

# objek3 memiliki isi sama, tetapi merupakan objek baru
object3_3025 = data_3025.copy()

print("object1 =",object1_3025)
print("object2 =",object2_3025)
print("object3 =",object3_3025)

# Operator is
hasil_3025 = object1_3025 is object2_3025
print("\nOperator identitas IS")
print("objek1 is objek2 =",hasil_3025)

# Operator is not
hasil_3025 = object1_3025 is not object2_3025
print("\nOperator identitas IS NOT")
print("objek1 is not objek2 =",hasil_3025)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =",object1_3025 is object3_3025)
print("objek1 == objek3 =",object1_3025 == object3_3025)