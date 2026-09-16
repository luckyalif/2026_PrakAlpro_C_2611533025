print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3025 = input("Masukkan Nama Mahasiswa : ")
kelamin_3025 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3025 = int(input("Masukkan Umur : "))
skor_3025 = float(input("Masukkan Skor Tes Awal : "))

alamat_3025 = """
Koto Luar,
Kecamatan Pauh,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_3025: Final = 75.0
token_3025 = 100+3j
lulus_3025 = skor_3025 > kkm_3025

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_3025," | ",type(nama_3025))
print("Jenis Kelamin : ",kelamin_3025," | ",type(kelamin_3025))
print("Alamat Domisili : ",alamat_3025," | ",type(alamat_3025))
print("Umur : ",umur_3025," tahun | ",type(umur_3025))
print("Skor Tes Awal : ",skor_3025," | ",type(skor_3025))
print("ID Token Sinyal: ",token_3025," | ",type(token_3025))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_3025," | ",type(kkm_3025))
print("Apakah Dinyatakan Lulus?: ",lulus_3025," | ",type(lulus_3025))