a = input('nama: ')
g =[]
m =[]
for i in a:
    S = (ord(i)+3)
    g.append(S)

for j in g:
    K = chr(j)
    m.append(K)
l = "".join(m)

print(f'nama setelah enkripsi: {l}')
