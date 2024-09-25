#Hanan Fijananto - 538946
#Nadhira Farra Aisya S - 535556
#Rizki Nur Ikhsan - 544540

apotek = []
batas_stok_rendah = 5
total_pemasukan = 0

while True:
    print("Sistem Apotek\n")
    print("Menu:")
    print("|  1. Tambah Obat                 |")
    print("|  2. Lihat Stok Obat             |")
    print("|  3. Hapus Obat                  |")
    print("|  4. Jual Obat                   |")
    print("|  5. Laporan Transaksi Obat      |")
    print("|  6. Peringatan Stok Rendah      |")
    print("|  7. Peringatan Obat Kadaluarsa  |")
    print("|  8. Laporan Keuangan            |")
    print("|  9. Diskon dan Promosi          |")
    print("|  10. Keluar                     |")
    print("___________________________________\n")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        nama = input("Nama Obat: ")
        stok = int(input("Stok Obat: "))
        harga = float(input("Harga Obat: "))
        tanggal_kadaluarsa = input("Tanggal Kadaluarsa (YYYY-MM-DD): ")
        tanggal_split = tanggal_kadaluarsa.split('-')
        tanggal_kadaluarsa_obat = list(map(int, tanggal_split))
        # tanggal_kadaluarsa = input("Tanggal Kadaluarsa (YYYY MM DD): ").split()
        # tanggal_kadaluarsa_obat = list(map(int, tanggal_kadaluarsa))

        # obat_baru = {
        #     "tanggal obat": tanggal_kadaluarsa_obat
        # }

        apotek.append([nama, stok, harga, tanggal_kadaluarsa, ])
        print('Obat', nama, 'berhasil ditambahkan dengan stok', stok, 'hingga: ',tanggal_kadaluarsa)

    elif pilihan == '2':
        print("Stok Obat:")
        for i in apotek:
            print(f"Nama: {i[0]}, Stok: {i[1]}, Harga/pcs: {i[2]}")

    elif pilihan == '3':
        nama = input("Nama Obat yang ingin dihapus: ")
        for i in apotek:
            if i[0] == nama:
                apotek.remove(i)
                print(f"Obat '{nama}' berhasil dihapus.")
                break
        else:
            print(f"Obat '{nama}' tidak ditemukan.")

    elif pilihan == '4':
        nama = input("Nama Obat yang dijual: ")
        jumlah = int(input("Jumlah yang dijual: "))
        tanggal_beli = list(map(int,input("masukan tanggal beli (YYYY MM DD): ").split()))

        for obat in apotek:
            if obat[0] == nama:
                if obat[2] == harga:
                    if obat[1] >= jumlah:
                        obat[1] -= jumlah
                        total_harga = obat[2] * jumlah
                        total_pemasukan += total_harga
                        print(f"Obat '{nama}' terjual sebanyak {jumlah}. Total harga: {total_harga}")
                        print(f"Sisa Stok {obat[1]}.")

                elif obat[2] < harga:
                    if obat[1] >= jumlah:
                        obat[1] -= jumlah
                        total_harga_diskon = harga_setelah_diskon * jumlah
                        total_pemasukan += total_harga
                        print(f"Obat '{nama}' terjual sebanyak {jumlah}. Total harga: {total_harga_diskon}")
                        print(f"Sisa Stok {obat[1]}.")

                else:
                    print(f"Stok '{nama}' tidak cukup.")
                break
        else:
            print(f"Obat '{nama}' tidak ditemukan.")

    elif pilihan == '5':
        print("Laporan Transaksi Obat:")
        for obat in apotek:
            print(f"Nama obat: {obat[0]}, jumlah yang sudah terjual: {jumlah} obat, Stok Tersisa: {obat[1]}, Total Harga : {total_harga} Tanggal pembelian: {tanggal_beli}")

    elif pilihan == '6':
        print("Peringatan Stok Rendah:")
        for obat in apotek:
            if obat[1] < batas_stok_rendah:
                print(f"Stok obat {obat[0]} memiliki stok rendah: {obat[1]}")
            else:
                print(f"Stok obat {nama} masih aman")

    elif pilihan == '7':
        hari_ini = list(map(int,input("masukan tanggal hari ini (YYYY MM DD): ").split()))
        nama_obat = input('masukkan nama obat: ')
        for i in apotek:    
            if i[0] == nama_obat:
                if tanggal_kadaluarsa_obat[0] == hari_ini[0]:
                    if tanggal_kadaluarsa_obat[1] <= hari_ini[1]:
                        if tanggal_kadaluarsa_obat[2] <= hari_ini[2]: 
                            print(f"Hati-hati! obat {nama} dengan tanggal kadaluarsa {tanggal_kadaluarsa}, sudah kadaluarsa!")
                        else:
                            print(f"Obat {nama_obat} dengan tanggal kadaluarsa {tanggal_kadaluarsa} belum kadaluarsa!")
                    else: 
                        print(f"Obat {nama_obat} dengan tanggal kadaluarsa {tanggal_kadaluarsa} belum kadaluarsa!")
                
                        
                elif tanggal_kadaluarsa_obat[0] < hari_ini[0]:
                    if tanggal_kadaluarsa_obat[1] <= hari_ini[1] or tanggal_kadaluarsa_obat[1] >= hari_ini [1]:
                        if tanggal_kadaluarsa_obat[2] <= hari_ini[2] or tanggal_kadaluarsa_obat[2] >= hari_ini[2]: 
                            print(f"Hati-hati! obat {nama} dengan tanggal kadaluarsa {tanggal_kadaluarsa}, sudah kadaluarsa!")
                        else:
                            print(f"Obat {nama_obat} dengan tanggal kadaluarsa {tanggal_kadaluarsa} belum kadaluarsa!")
                    else:
                        print(f"Obat {nama_obat} dengan tanggal kadaluarsa {tanggal_kadaluarsa} belum kadaluarsa!")
                else:
                    print(f"Obat {nama_obat} dengan tanggal kadaluarsa {tanggal_kadaluarsa} belum kadaluarsa!")
            else:
                    print(f"Obat {nama_obat} dengan tanggal kadaluarsa {tanggal_kadaluarsa} belum kadaluarsa!")


    elif pilihan == '8':
        total_pengeluaran = 0
        for obat in apotek:
            total_pengeluaran += obat[2] * obat[1]  
        print(f"Laporan Keuangan:")
        print(f"Total Pendapatan: {total_pemasukan}")
        # print(f"Total Pemasukan: {total_pemasukan}")
        # print(f"Total Pengeluaran: {total_pengeluaran}")
        # print(f"Sisa Keuntungan: {total_pemasukan - total_pengeluaran}")


    elif pilihan == '9':
        nama_diskon = input("Nama Obat untuk diskon: ")
        diskon = float(input("Persentase diskon (misal 10 untuk 10%): ")) / 100
        for obat in apotek:
            if obat[0] == nama_diskon:
                harga_setelah_diskon = obat[2] * (1 - diskon)
                akhir = obat[2] - harga_setelah_diskon
                obat[2] = akhir
                print(f"Harga '{nama_diskon}' setelah diskon: {harga_setelah_diskon}")
                break
        else:
            print(f"Obat '{nama_diskon}' tidak ditemukan.")


    elif pilihan == '10':
        print("Sistem apotek ditutup.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")