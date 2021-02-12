from typing import List


def build_max_heap(arr: List[int]) -> None:
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i, len(arr))


def max_heapify(arr: List[int], i: int, size: int = None) -> int:
    if size is None:
        size = len(arr)

    l = left(i)
    r = right(i)
    largest = None
    if l < size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, size)


def parent(i: int) -> int:
    return ((i + 1) // 2) - 1


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def heap_sort(arr: List[int]) -> None:
    build_max_heap(arr)
    size = len(arr)
    for i in range(size-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        size -= 1
        max_heapify(arr, 0, size)
