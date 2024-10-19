# latihan 3
anggota = {}
while True:
    print('1. Daftar anggota baru')
    print('2. Pinjam buku baru')
    print('3. Hapus buku')
    print('4. Daftar angoota pinjam')
    print('5. Keluar Program')

    pilih = int(input('pilih menu: '))
    if pilih == 1:
        orang = input('masukkan nama anggota: ')
        # buku = input('masukkan buku yang ingin dipinjam: ').split()
        buku = input('buku yang dipinjam: ').split()
        anggota[orang] = buku
        print(anggota)

    elif pilih == 2:
        orang_baru = input('masukkan nama anggota: ')
        if orang_baru in anggota:
            buku_baru = input('masukkan buku yang ingin ditambahkan: ')
            # baru =  buku.append(buku_baru)
            anggota[orang_baru].append(buku_baru)
        else:
            print('nama tidak ditemukan')
    
    elif pilih == 3:
        hapus_nama = input('masukkan nama anggota: ')
        if hapus_nama in anggota:
            hapus_buku = input('Buku yang ingin dihapus: ')
            buku.remove(hapus_buku)
        else:
            print('nama tidak ditemukan')

    elif pilih == 4:
        for key, values in anggota.items(): 
            print(key,':', values)
    
    else:
        print('keluar dari program')
        break
