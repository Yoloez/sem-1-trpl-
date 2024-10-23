def tambah(a, b):
    if a + b == 1:
        return 1
    else:
        k = a + b
        print(k)
        return(tambah(a, b-1))
print(tambah(5, 1))