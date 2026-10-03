print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_3025 = int(input("Masukkan ukuran skala jam pasir (N): "))

# ---------- Bingkai atas ----------
print("#", end="")
for pagar_3025 in range(4 * n_3025 + 5):
    print("=", end="")
print("#", end="")
print()

# ---------- Fase 1: jam pasir atas (N turun s.d. 1) ----------
for baris_3025 in range(n_3025, 0, -1):
    print("| ", end="")
    for spasi_kiri_3025 in range(2 * (n_3025 - baris_3025)):
        print(" ", end="")
    for angka_3025 in range(baris_3025, 0, -1):
        print(angka_3025, end=" ")
    print("<*>", end="")
    for angka_3025 in range(1, baris_3025 + 1):
        print(" ", end="")
        print(angka_3025, end="")
    for spasi_kanan_3025 in range(2 * (n_3025 - baris_3025)):
        print(" ", end="")
    print(" |", end="")
    print()

# ---------- Fase 2: poros titik pusat ----------
print("|", end="")
for spasi_kiri_3025 in range(2 * n_3025 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_kanan_3025 in range(2 * n_3025 + 1):
    print(" ", end="")
print("|", end="")
print()

# ---------- Fase 3: jam pasir bawah (1 naik s.d. N) ----------
for baris_3025 in range(1, n_3025 + 1):
    print("| ", end="")
    for spasi_kiri_3025 in range(2 * (n_3025 - baris_3025)):
        print(" ", end="")
    for angka_3025 in range(baris_3025, 0, -1):
        print(angka_3025, end=" ")
    print("<*>", end="")
    for angka_3025 in range(1, baris_3025 + 1):
        print(" ", end="")
        print(angka_3025, end="")
    for spasi_kanan_3025 in range(2 * (n_3025 - baris_3025)):
        print(" ", end="")
    print(" |", end="")
    print()

# ---------- Bingkai bawah ----------
print("#", end="")
for pagar_3025 in range(4 * n_3025 + 5):
    print("=", end="")
print("#", end="")
print()