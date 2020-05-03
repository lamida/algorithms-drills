arr = [2, 10, 1, 0, 7]

for i in range (1, len(arr)):
    for i in range(i, 0, -1):
        if arr[i-1] > arr[i]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

