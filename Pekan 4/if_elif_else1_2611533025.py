# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_3025 = int(input("Input Umur Anda: "))
sim_3025 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_3025 >= 17 and sim_3025 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_3025 >= 17 and sim_3025 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3025 < 17 and sim_3025     == "y":
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai")