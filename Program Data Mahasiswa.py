#Hanan Fijananto
#no 1 data mahasiswa dan enkripsi
mhs_lulus = []#variabel yang berisi data mahasiswa yang nilainya 70 keatas
data = {} #dictionary yang berisi data nama mahasiswa asli, terenkripsi, usia, dan nilai rata-rata

while True:   
    print('RUANG DATA MAHASISWA TERENKRIPSI')
    print('Menu:')
    print('1. Tambah Data Mahasiswa')
    print('2. Tampilkan Data Mahasiswa (Terenkripsi)')
    print('3. Tampilkan Nama Asli Mahasiswa')
    print('4. Cari Mahasiswa Berdasarkan Nama')
    print('5. Hitung Rata-rata Nilai Mahasiswa')
    print('6. Tampilkan Mahasiswa yang Lulus (Terenkripsi)')
    print('7. Tampilkan Mahasiswa Tertua dan Termuda (Terenkripsi)')
    print('8. Keluar Program\n')
    pilih = int(input('Pilih Menu: '))

    def tambah (nama, usia, rata): #fungsi tambah yang digunakan untuk memasukkan data yang di-input ke dictionary (data)
        print(f'mahasiswa bernama {nama} dengan usia {usia} tahun dan nilai rata-rata {rata} berhasil ditambahkan')
        data[nama] = {
        "Nama" : nama_enkrip,
        "Usia" : usia,
        'Rata-rata' : rata
        }

    def konversi(x): #fungsi yang digunakan untuk mengonversikan nama asli menjadi nama enkripsi
        for i in data:  
            jeneng = data[i]['Nama'] #jeneng adalah variabel yang digunakan untuk melihat nama asli pada data
            if jeneng == x: #jika nama asli sama dengan nama asli yang telah di-lower, maka jalankan program di bawah
                abjad_nama = [] 
                hasil_enkripsi = []
                for huruf in jeneng: #untuk setiap huruf di dalam nama asli, maka buat variabel karakter
                    karakter = ord(huruf) + 3 #variabel karakter berisi huruf yang dikonversikan ke dalam angka (ord) sesuai ASCII lalu ditambah 3 sesuai aturan dalam soal
                    abjad_nama.append(karakter) #setiap huruf yang telah dikonversikan sebelumnya, akan dimasukkan ke dalam list abjad_nama
                for j in abjad_nama:#Untuk setiap j (huruf) dalam list abjad_nama yang pasti sudah berisi semua huruf yang telah dikonversikan ke ord, maka jalankan program di bawah
                    if j == 123:  #jika j sama dengan 123 (huruf x dalam ASCII) maka j diubah menjadi 97 (huruf a dalam ASCII)
                        j = 97
                    elif j == 124: #jika j sama dengan 124 (huruf y dalam ASCII) maka j diubah menjadi 98 (huruf b dalam ASCII)
                        j = 98
                    elif j == 125: #jika j sama dengan 125 (huruf z dalam ASCII) maka j diubah menjadi 99 (huruf c dalam ASCII)
                        j = 99
                    elif j == 32:
                        j = ''
                    enkrip = chr(j) #variabel enkrip berfungsi untuk mengubah angka ASCII ke dalam huruf karena ada (chr)
                    hasil_enkripsi.append(enkrip) #variabel enkrip untuk setiap huruf tadi, dimasukkan ke list hasil_enkripsi
                    gabung = "".join(hasil_enkripsi) #karena setiap huruf masih terpisah, maka buat variabel gabung dengan fungsi join agar setiap huruf dapat digabung menjadi kata. 
                data[i]["Enkripsi"] = gabung

    def daftar_enkripsi(data): #fungsi untuk menu 2 yang menampilkan nama mahasiswa terenkripsi
        print('Daftar Mahasiswa (Terenkripsi):')
        nomor = 1
        for enk in data: #untuk setiap dictionary dalam dictionary maka tampilkan setiap dictionary dengan nama yang terenkripsi, usia, beserta nilai
            print(f'{nomor}. Nama Terenkripsi: {data[enk]["Enkripsi"]}, Usia: {data[enk]["Usia"]} Nilai: {data[enk]["Rata-rata"]}')
            nomor +=1

    def daftar_asli(data): #fungsi untuk menu 3 yang menampilkan nama mahasiswa asli
        nomor = 1
        print('Daftar Mahasiswa (Nama Asli): ')
        for asli in data: #untuk setiap dictionary dalam dictionary maka tampilkan setiap dictionary dengan nama asli, usia, beserta nilai
            print(f'{nomor}. Nama: {data[asli]["Nama"]}, Usia: {data[asli]["Usia"]}, Nilai: {data[asli]["Rata-rata"]}')
            nomor +=1 
    
    def mencari(data): #fungsi untuk menu 4 yang menampilkan nama mahasiswa yang dicari melalui input
        for pencarian in data: 
            if cari in data[pencarian]['Nama']: #jika variabel cari ada di dalam data nama, maka print di bawah ini
                print(f'mahasiwa {cari} ditemukan. Usia:', data[pencarian]['Usia'],'Nilai rata-rata:',data[pencarian]['Rata-rata'])
            if cari not in data[pencarian]['Nama']: #jika variable cari tidak ada di dalam data nama, maka print nama tidak ditemukan
                print('Nama tidak ditemukan')
                break
    

    def rata_rata (total): #fungsi untuk menu 5 yang menampilkan rata-rata seluruh nilai mahasiswa
        rata = total/len(data) #variabel rata untuk menghitung rata-rata dengan cara total seluruh nilai mahasiswa dibagi dengan banyaknya mahasiswa
        print(f'Rata-rata nilai seluruh mahasiswa: {rata}')

    def lulus(data): #fungsi untuk menu 6 yang menampilkan nama mahasiswa yang nilai rata-ratanya di atas 70
        for i in data: #untuk setiap i dalam data dictionary, jika rata-rata tiap mahasiswa di atas 70, maka nama mahasiswa yang terenkripsi dimasukkan ke dalam list mhs_lulus
            if data[i]['Rata-rata'] >= 70:
                mhs_lulus.append(data[i]['Enkripsi'])
        print(f'mahasiswa yang lulus(terenkripsi): ')
        for i in mhs_lulus: #memanggil list mhs_lulus agar tidak di dalam list
            print(i, end=', ')
        print('\n')

    def umur(data): #fungsi untuk menu no 7 yang menampilkan usia tertua dan termuda
        tua = 0 
        muda = float('inf') #tak hingga (paling besar)
        for i in data:
            data_usia = data[i]['Usia']
            if data_usia > tua: #jika usia mahasiswa lebih besar dari variabel tua, maka variabel tua diganti dengan usia mahasiswa, begitu seterusnya hingga menemukan usia mahasiswa tertua
                tua = data_usia
                paling_tua = data[i]['Enkripsi']
            if data_usia < muda:#jika usia mahasiswa lebih kecil dari variabel muda, maka variabel muda diganti dengan usia mahasiswa, begitu seterusnya hingga menemukan usia mahasiswa termuda
                muda = data_usia
                paling_muda = data[i]['Enkripsi']
        print(f'Mahasiswa tertua: {paling_tua}, Usia: {tua}')
        print(f'Mahasiswa termuda: {paling_muda}, Usia: {muda}')
            

    if pilih == 1:
        nama = input('Masukkan nama mahasiswa: ')
        nama_enkrip = nama.lower()
        usia = int(input('Masukkan usia mahasiswa: '))
        nilai = int(input('Masukkan nilai rata-rata mahasiswa: '))
        tambah(nama, usia, nilai)
        konversi(nama_enkrip)

    elif pilih == 2:
        # for value in data.items():
        daftar_enkripsi(data)
    
    elif pilih == 3:
        daftar_asli(data)

    elif pilih == 4:
        cari_asli = input('Masukkan nama mahasiswa yang ingin dicari: ')
        cari = cari_asli.lower()
        mencari(data)
                    
    elif pilih == 5:
        total = 0
        for semua in data: #untuk setiap dictionary dalam dictionary, variabel total ditambah dengan nilai dari setiap mahasiswa
            total += data[semua]['Rata-rata']
        print(rata_rata(total))

    elif pilih == 6:
        lulus(data)

    elif pilih == 7 :
        umur(data)

    elif pilih == 8:
        print('Keluar sistem')
        break

    else:
        print('Input tidak valid')
        print('Masukkan angka(1-8)')

