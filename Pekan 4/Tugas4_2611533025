"""
Tugas 4 - Sistem Loket Terpadu & Audit Transaksi Ekspedisi Wahana
Nama   : Lucky Alif Pratama
NIM    : 2611533025
Materi : if tunggal, if-else, if-elif-else (operator logika), multi-if terpisah, match-case
"""

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung & String Handling
nama_3025 = input("Masukkan Nama Pengunjung        : ")
umur_3025 = int(input("Input umur anda                 : "))
sim_3025 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

print()
print("Pilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")
paket_3025 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3025 = int(input("Masukkan jumlah tiket           : "))

# Validasi kelogisan jumlah tiket (if tunggal)
if jumlah_tiket_3025 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

# 2. Pemilihan Wahana menggunakan match-case
nama_wahana_3025 = ""
harga_satuan_3025 = 0
transaksi_valid_3025 = True

match paket_3025:
    case 1:
        nama_wahana_3025 = "Wahana Safari Rimba"
        harga_satuan_3025 = 50000
    case 2:
        nama_wahana_3025 = "Wahana Arung Jeram"
        harga_satuan_3025 = 75000
    case 3:
        nama_wahana_3025 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3025 = 120000
    case 4:
        nama_wahana_3025 = "Wahana Roller Coaster Kilat"
        harga_satuan_3025 = 100000
    case 5:
        nama_wahana_3025 = "Wahana All-Access VIP"
        harga_satuan_3025 = 220000
    case _:
        print("Paket wahana tidak valid!")
        transaksi_valid_3025 = False

if transaksi_valid_3025:
    is_member_3025 = input("Apakah Anda member? (y/t)       : ").strip().lower()
    kode_promo_valid_3025 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

    print()
    print("--- KELAYAKAN PENGENDARA WAHANA ---")

    # 3. Validasi izin kendali wahana (if-elif-else dengan operator logika)
    if paket_3025 == 3:
        if umur_3025 >= 17 and sim_3025 == 'y':
            print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
        elif umur_3025 >= 17 and sim_3025 != 'y':
            print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_3025 < 17 and sim_3025 == 'y':
            print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
    else:
        # Untuk paket selain 3, if-else sederhana cek umur >= 10 tahun
        if umur_3025 >= 10:
            print("Status Akses: Anda memenuhi syarat umur untuk menaiki wahana ini.")
        else:
            print("Status Akses: Anda belum memenuhi syarat umur untuk menaiki wahana ini.")

    # 4. Akumulasi diskon bertingkat (multi-if terpisah)
    subtotal_3025 = harga_satuan_3025 * jumlah_tiket_3025
    total_diskon_persen_3025 = 0

    if subtotal_3025 >= 200000:
        total_diskon_persen_3025 += 10  # Diskon Belanja Besar

    if is_member_3025 in ['y', 'ya']:
        total_diskon_persen_3025 += 5  # Diskon Member

    if kode_promo_valid_3025 in ['y', 'ya']:
        total_diskon_persen_3025 += 15  # Diskon Voucher Promo

    if jumlah_tiket_3025 >= 5:
        total_diskon_persen_3025 += 5  # Diskon Tambahan Rombongan

    # 5. Evaluasi kelulusan audit (if-else)
    nominal_diskon_3025 = subtotal_3025 * (total_diskon_persen_3025 / 100)
    total_bayar_3025 = subtotal_3025 - nominal_diskon_3025

    if total_bayar_3025 > 300000:
        catatan_layanan_3025 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
    else:
        catatan_layanan_3025 = "Terima kasih telah berkunjung."

    print()
    print("--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp {subtotal_3025:,.0f}")
    print(f"Total Diskon     : {total_diskon_persen_3025}% (Rp {nominal_diskon_3025:,.0f})")
    print(f"Total Bayar      : Rp {total_bayar_3025:,.0f}")
    print(f"Catatan Layanan  : {catatan_layanan_3025}")
    print("Program Selesai")