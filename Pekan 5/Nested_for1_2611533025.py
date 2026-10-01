# Buat file dengan nama Nested_for1_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_3025 = int(input("Masukkan nilai batas: "))
for line_3025 in range(1, batas_3025 + 1):
    for j_3025 in range(1, (-1 * line_3025 + batas_3025) + 1):
        print(".", end=" ")
    print(line_3025)