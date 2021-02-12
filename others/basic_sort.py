def insertion_sort(arr):
    i = 1
    while i < len(arr):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        i += 1

# https://www.youtube.com/watch?v=Kg4bqzAqRBM&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=3&ab_channel=MITOpenCourseWare
def insertion_sort_mit(arr):
    key = 1
    while key < len(arr):
        j = key
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        key += 1


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

arr2 = [5, 2, 4, 6, 1, 3]
insertion_sort_mit(arr2)
print(arr2)
