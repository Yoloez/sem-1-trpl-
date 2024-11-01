# Hanan Fijananto

#no 2 
def konversi(x):
    huruf_besar = 0 #variabel yang digunakan untuk membandingkan banyaknya huruf besar dan kecil
    huruf_kecil = 0 #variabel yang digunakan untuk membandingkan banyaknya huruf besar dan kecil
    
    for kata in x:
        if kata.islower(): #melihat setiap huruf, jika huruf kecil, maka variabel huruf_kecil ditambah satu, jika huruf besar, variabel huruf_besar ditambah 1
            huruf_kecil+=1
        else:
            huruf_besar+=1
        
    if huruf_kecil > huruf_besar: #Jika banyak variabel huruf_kecil lebih besar dari variabel huruf_besar, maka mengembalikan nilai x kecil semua.
        return x.lower()
    elif huruf_besar == huruf_kecil: #jika banyak variabel huruf_kecil sama dengan variabel huruf_besar, maka mengembalikan nilai x sesuai huruf terakhir kata. 
        if x[-1].islower(): #jika huruf terakhir kecil, maka kata dikembalikan dengan huruf kecil
            return x.lower()
        else:   #jika huruf terakhir kapital, maka kata dikembalikan dengan huruf kapital
            return x.upper()
    else: #Jika banyak variabel huruf_besar lebih besar dari variabel huruf_kecil, maka mengembalikan nilai x kapital semua.
        return x.upper()

nama = input('Nama: ').split() #input

for i in nama: #membuat perulangan agar setiap kata pada kalimat dapat dihitung satu-satu.
    print(konversi(i), end=' ')
