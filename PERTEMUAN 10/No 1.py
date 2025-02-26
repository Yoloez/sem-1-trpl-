P, Q = map(int, (input().split()))
total = (P*P) + (Q*Q) + 1
hasil = total % 4
if hasil > 0:
    print(-1)
if hasil == 0:
    print(total/4)