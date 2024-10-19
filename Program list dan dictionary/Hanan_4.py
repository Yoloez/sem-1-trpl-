# latihan 4
meja = {
    1 : 'kosong',
    2 : 'kosong',
    3 : 'kosong',
    4 : 'kosong',
}
while True:
    print('1. Pesan Meja')
    print('2. Hapus Pesanan meja')
    print('3. Status Meja')
    print('4. Keluar Program')
    pilih = int(input('pilih menu: '))

    if pilih == 1:
        nama = input('masukkan nama: ')
        pilih_meja = int(input('pilih meja: (1-4) '))
        if meja[pilih_meja] != 'kosong':
            print('Meja sudah dipesan')
        elif pilih_meja in meja:
            meja[pilih_meja] = nama

    elif pilih == 2:
        hapus = int(input('hapus reservasi dengan no meja: '))
        if hapus in meja:
            meja[hapus] = 'kosong'

    elif pilih == 3:
        print(meja)
    
    else:
        print('keluar dari program')
        break