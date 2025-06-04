def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah  # nilai ditemukan
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1  # tidak ditemukan

# === Program dengan Menu ===
nilai_mahasiswa = []

while True:
    print("\n=== MENU PROGRAM NILAI MAHASISWA ===")
    print("1. Input nila/Input ulang nilai mahasiswa")
    print("2. Cari nilai dalam daftar (binary search)")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        nilai_mahasiswa.clear()
        n = int(input("Masukkan jumlah nilai mahasiswa: "))
        for i in range(n):
            nilai = int(input(f"Nilai mahasiswa ke-{i+1}: "))
            nilai_mahasiswa.append(nilai)
        nilai_mahasiswa.sort()
        print("Nilai berhasil disimpan dan diurutkan:", nilai_mahasiswa)

    elif pilihan == '2':
        if not nilai_mahasiswa:
            print("Data masih kosong. Silakan input nilai terlebih dahulu (pilih menu 1).")
        else:
            cari = int(input("Masukkan nilai yang ingin dicari: "))
            index = binary_search(nilai_mahasiswa, cari)
            if index != -1:
                print(f"Nilai {cari} ditemukan pada indeks ke-{index} (setelah diurutkan).")
            else:
                print(f"Nilai {cari} tidak ditemukan dalam daftar.")

    elif pilihan == '3':
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
