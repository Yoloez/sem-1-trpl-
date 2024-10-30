N, M = map(int, input().split())
if N % 2 == 0 and M % 2 == 0:
    hasil = M * N
    print(hasil)
else:
    print('input harus angka genap')