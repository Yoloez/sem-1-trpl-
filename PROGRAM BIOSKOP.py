film = []
daftar_film = ['Naruto', 'Batman', 'Venom']
daftar_kursi1 = ['A1', 'A2', 'A3', 'A4']
daftar_kursi2 = ['A5', 'A6', 'A7', 'A8']
daftar_kursi3 = ['A1', 'A2', 'A3', 'A4']
daftar_kursi4 = ['A1', 'A2', 'A3', 'A4']
daftar_kursi5 = ['A1', 'A2', 'A3', 'A4']
daftar_kursi6 = ['A1', 'A2', 'A3', 'A4']
jam = ['12.00', '20.00', '13.00', '21.00', '15.00', '17.00']
while True:
    print('\n')
    print('| SELAMAT DATANG DI BIOSKOP MODERN |\n')
    print(' silahkan pilih menu di bawah ini ')
    print('| 1. Lihat Film dan Jadwal Tayang|')
    print('| 2. Pesan Tiket                 |')
    print('| 3. Lihat Pemesanan             |')
    print('| 4. Cek Ketersediaan Kursi      |')
    print('| 5. Keluar                      |\n')

    pilihan = int(input('Pilih Menu: '))
    if pilihan == 1:
        print('Daftar Film yang sedang tayang:')
        print('1. Naruto, Jam tayang: 12.00 dan 20.00')
        print('2. Batman, Jam tayang: 13.00 dan 21.00')
        print('3. Venom, Jam tayang: 15.00 dan 17.00')

    elif pilihan == 2:
        print('Daftar Film yang sedang tayang:')
        print('1. Naruto')
        print('2. Batman')
        print('3. Venom')
        pilih_film = (input('Pilih film yang akan dipesan (Naruto): '))
        if pilih_film == 'Naruto':
            print('jadwal tayang film Naruto:')
            print('1. 12.00')
            print('2. 20.00')
            jam_tayang = input('pilih jam tayang (15.00): ')
            if jam_tayang == '12.00':
                print('daftar kursi yang tersedia: ')
                print(daftar_kursi1)
                pilih_kursi = input('pilih nomor kursi (A1-A4): ')
                if pilih_kursi not in daftar_kursi1:
                    print('Kursi tidak tersedia')
                else:
                    daftar_kursi1.remove(pilih_kursi)
                    print('Tiket berhasil dipesan untuk film',f'{pilih_film} pada {jam_tayang}, kursi: {pilih_kursi}. Harga: Rp100,000')
            elif jam_tayang == '20.00':
                print('daftar kursi yang tersedia: ')
                print(daftar_kursi2)
                pilih_kursi = input('pilih nomor kursi (A1-A4): ')
                if pilih_kursi not in daftar_kursi2:
                    print('Kursi tidak tersedia')
                else:
                    daftar_kursi2.remove(pilih_kursi)
                    print('Tiket berhasil dipesan untuk film',f'{pilih_film} pada {jam_tayang}, kursi: {pilih_kursi}. Harga: Rp100,000')
            else:
                print('jam tayang tidak tersedia')
  
        elif pilih_film == 'Batman':
            print('jadwal tayang film Batman:')
            print('1. 13.00')
            print('2. 21.00')
            jam_tayang = input('pilih jam tayang (15.00): ')
            if jam_tayang == '13.00':
                print('daftar kursi yang tersedia: ')
                print(daftar_kursi3)
                pilih_kursi = input('pilih nomor kursi (A1-A4): ')
                if pilih_kursi not in daftar_kursi3:
                    print('Kursi tidak tersedia')
                else:
                    daftar_kursi3.remove(pilih_kursi)
            elif jam_tayang == '21.00':
                print('daftar kursi yang tersedia: ')
                print(daftar_kursi4)
                pilih_kursi = input('pilih nomor kursi (A1-A4): ')
                if pilih_kursi not in daftar_kursi4:
                    print('Kursi tidak tersedia')
                else:
                    daftar_kursi4.remove(pilih_kursi)
            else:
                print('jam tayang tidak tersedia')
            
        elif pilih_film == 'Venom':
            print('jadwal tayang film Venom:')
            print('1. 15.00')
            print('2. 17.00')
            jam_tayang = input('pilih jam tayang (15.00): ')
            if jam_tayang == '15.00':
                print('daftar kursi yang tersedia: ')
                print(daftar_kursi5)
                pilih_kursi = input('pilih nomor kursi (A1-A4): ')
                if pilih_kursi not in daftar_kursi5:
                    print('Kursi tidak tersedia')
                else:
                    daftar_kursi5.remove(pilih_kursi)
            elif jam_tayang == '17.00':
                print('daftar kursi yang tersedia: ')
                print(daftar_kursi6)
                pilih_kursi = input('pilih nomor kursi (A1-A4): ')
                if pilih_kursi not in daftar_kursi6:
                    print('Kursi tidak tersedia')
                else:
                    daftar_kursi6.remove(pilih_kursi)
            else:
                print('jam tayang tidak tersedia')

        else:
            print('film tidak tersedia')
                   
        film.append({'nama': pilih_film, 'jam tayang': jam_tayang, 'kursi': pilih_kursi, 'harga': 'Rp100,000'})

    elif pilihan == 3:
        if not film:
            print('Kamu belum memesan tiket')
        else:
            for i in film:
                print(f"Film: {i['nama']}, jam tayang: {i['jam tayang']}, kursi: {i['kursi']}, harga: {i['harga']}")
            
    elif pilihan == 4:
        print('Daftar Film yang sedang tayang:')
        print('1. Naruto')
        print('2. Batman')
        print('3. Venom')
        pilih_film = (input('Cek kursi pada film (Naruto): '))
        if pilih_film == 'Naruto':
            print('jadwal tayang film Naruto:')
            print('1. 12.00')
            print('2. 20.00')
            jam_tayang = input('pilih jam tayang (15.00): ')
            if jam_tayang == '12.00':
                print('daftar kursi yang tersedia: ')
                if len(daftar_kursi1) == 4:
                    print(daftar_kursi1)
                elif len(daftar_kursi1) > 0:
                    print(daftar_kursi1)
                else:
                    print('kursi telah habis')
               
            if jam_tayang == '20.00':
                print('daftar kursi yang tersedia: ')
                if len(daftar_kursi2) == 4:
                    print(daftar_kursi2)
                elif len(daftar_kursi2) > 0:
                    print(daftar_kursi2)
                else:
                    print('kursi telah habis')
               
  
        elif pilih_film == 'Batman':
            print('jadwal tayang film Batman:')
            print('1. 13.00')
            print('2. 21.00')
            jam_tayang = input('pilih jam tayang (15.00): ')
            if jam_tayang == '13.00':
                print('daftar kursi yang tersedia: ')
                if len(daftar_kursi3) == 4:
                    print(daftar_kursi3)
                elif len(daftar_kursi3) > 0:
                    print(daftar_kursi3)
                else:
                    print('kursi telah habis')

            if jam_tayang == '21.00':
                print('daftar kursi yang tersedia: ')
                if len(daftar_kursi4) == 4:
                    print(daftar_kursi4)
                elif len(daftar_kursi4) > 0:
                    print(daftar_kursi4)
                else:
                    print('kursi telah habis')
            

        elif pilih_film == 'Venom':
            print('jadwal tayang film Venom:')
            print('1. 15.00')
            print('2. 17.00')
            jam_tayang = input('pilih jam tayang (15.00): ')
            if jam_tayang == '15.00':
                print('daftar kursi yang tersedia: ')
                if len(daftar_kursi5) == 4:
                    print(daftar_kursi5)
                elif len(daftar_kursi5) > 0:
                    print(daftar_kursi5)
                else:
                    print('kursi telah habis')
            if jam_tayang == '17.00':
                print('daftar kursi yang tersedia: ')
                if len(daftar_kursi6) == 4:
                    print(daftar_kursi6)
                elif len(daftar_kursi6) > 0:
                    print(daftar_kursi6)
                else:
                    print('kursi telah habis')

    elif pilihan == 5:
        break

    else:
        print('Menu tidak tersedia (pilih angka 1-5)')