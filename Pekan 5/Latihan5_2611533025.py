batas_3025 = int(input("Masukkan nilai segi tiga: "))
for i_3025 in range(1, batas_3025 + 1):
    for j_3025 in range(batas_3025 - i_3025):
        print(" ", end="")
    for k_3025 in range(i_3025):
        print("*", end=" ")
    print() 

