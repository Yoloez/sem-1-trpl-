# Latihan 1
daftar_barang = []
harga_list = []
list_global = []
penjualan_hari_ini = {}
rincian_penjualan = {}
total = 0
while True:
    print('1. Input barang')
    print('2. jumlah barang yang dijual')
    print('3. Rincian penjualan')
    print('4. Keluar')
    pilih = int(input('pilih menu: '))
    
    if pilih == 1:
        barang = input('masukkan barang: ')
        daftar_barang.append(barang)
        jual = int(input('masukkan harga: '))
        harga_list.append(jual)
        list_global.append([barang, jual])
        print('Daftar barang:',daftar_barang)
        print('Harga:',harga_list)
        
    elif pilih == 2:
        jual_barang = input('masukkan barang yang akan dijual: ')
        for i in list_global:
            if i[0] == jual_barang:
                jual = int(input('jumlah barang yang dijual: '))
                harga = i[1] * jual
                total += harga
                penjualan_hari_ini[jual_barang] = jual
                rincian_penjualan[jual_barang] = harga
        print('Penjualan hari ini:',penjualan_hari_ini)

    elif pilih == 3:
        print('Rincian penjualan:',rincian_penjualan)
        print('Total pendapatan: Rp',total)

    else:
        print('keluar program')
        break
