# Buat file dengan nama Nested_for4_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_3025 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3025 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3025 = tinggi_3025
    c_3025 = a_3025 
    lebar_3025 = (2 * tinggi_3025) - 2

    for i_3025 in range(1, tinggi_3025 + 1):
        b_3025 = c_3025 + 1

        for j_3025 in range(1, lebar_3025 + 1):

            #Baris atas dan bawah
            if i_3025 == 1 or i_3025 == tinggi_3025:
                if j_3025 == 1 or j_3025 == lebar_3025:
                    print("#", end="")
                else:
                    print("=", end="")

            #Baris isi
            else:
                if j_3025 == 1 or j_3025 == lebar_3025:
                    print("|", end="")
                else:
                    if j_3025 == c_3025:
                        print("<", end="")
                    elif j_3025 == b_3025:
                        print(">", end="")
                    elif j_3025 == (lebar_3025 - c_3025):
                        print("<", end="")
                    elif j_3025 == (lebar_3025 - c_3025 + 1):
                        print(">", end="")
                    elif j_3025 > b_3025 and j_3025 < (lebar_3025 - c_3025):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # logika asli Java
        a_3025 -= 2

        if a_3025 <= 0:
            c_3025 = (-a_3025) + 2
        else:
            c_3025 = a_3025