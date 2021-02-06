def insertion_sort(arr):
    i = 1
    while i < len(arr):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        i += 1

def selection_sort(arr):
    i = 0
    while i < len(arr):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        i += 1

arr = [2, 10, 1, 0, 7, 1, 2, 100, 1000, -1]
insertion_sort(arr)
print(arr)

