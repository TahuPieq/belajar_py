def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    indices = []

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            indices.append(mid)
            # Mencari indeks di sebelah kiri
            left_index = mid - 1
            while left_index >= 0 and arr[left_index] == target:
                indices.append(left_index)
                left_index -= 1
            # Mencari indeks di sebelah kanan
            right_index = mid + 1
            while right_index < len(arr) and arr[right_index] == target:
                indices.append(right_index)
                right_index += 1
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return sorted(indices)

def input_nilai():
    print("Masukkan nilai mahasiswa (pisahkan dengan spasi):")
    input_str = input()
    try:
        nilai_list = list(map(int, input_str.strip().split()))
        nilai_list.sort()
        return nilai_list
    except ValueError:
        print("Input tidak valid. Masukkan angka dengan benar.")
        return None

def cari_nilai(nilai_mahasiswa):
    if not nilai_mahasiswa:
        print("Daftar nilai masih kosong. Silakan input nilai terlebih dahulu.")
        return

    try:
        nilai_target = int(input("Masukkan nilai yang ingin dicari: "))
    except ValueError:
        print("Input tidak valid, masukkan angka.")
        return

    indeks_ditemukan = binary_search(nilai_mahasiswa, nilai_target)
    if indeks_ditemukan:
        print(f"Nilai {nilai_target} ditemukan pada indeks: {indeks_ditemukan}")
    else:
        print(f"Nilai {nilai_target} tidak ditemukan dalam daftar.")

def main():
    nilai_mahasiswa = []
    while True:
        print("\nMenu:")
        print("1. Input nilai/Input ulang nilai")
        print("2. Cari nilai dalam indeks")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")
        if pilihan == '1':
            nilai_baru = input_nilai()
            if nilai_baru is not None:
                nilai_mahasiswa = nilai_baru
                print(f"Daftar nilai berhasil diupdate: {nilai_mahasiswa}")
        elif pilihan == '2':
            cari_nilai(nilai_mahasiswa)
        elif pilihan == '3':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
