def bubblesort(arr):
    panjang = len(arr)
    for i in range(panjang):
        for j in range(0, panjang-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 2, 7, 3, 9, 13, 6]
print(bubblesort(arr))
