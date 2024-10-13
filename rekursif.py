def rekursif(x):
    if x == 1:
        return 1
    else:
        return x * rekursif(x-1)
    
print(rekursif())


