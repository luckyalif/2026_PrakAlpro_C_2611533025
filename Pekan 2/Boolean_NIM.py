is_lulus = True
is_cumlaude =True

# Menggunakan Boolean
nilai_3025 = 85
batas_lulus_3025 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai_3025 >= batas_lulus_3025 # Hasilnya True

print ("=== Check Kelulusan ===")
print ("Nilai: ",nilai_3025)
print ("Apakah Lulus? :", status_kelulusan)
if is_lulus and is_cumlaude:
    print ("Selamat, Anda lulus dengan predikat Cum laude!")
    