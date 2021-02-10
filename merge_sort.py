# This is ridiculous, but I am still loss in merge sort :(
import random
from typing import List


def merge(arr: List[int], lo: int, mid: int, hi: int):
    i = lo 
    j = mid + 1

    aux = arr.copy()

    for k in range(lo, hi+1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:  # why len - 1?
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1


def sort(arr: List[int], lo: int, hi: int):
    if hi <= lo:
        return
    mid = lo + (hi-lo)//2
    sort(arr, lo, mid)
    sort(arr, mid+1, hi)
    merge(arr, lo, mid, hi)


def merge_sort(arr: List[int]):
    sort(arr, 0, len(arr)-1)


if __name__ == "__main__":
    for i in range(10):
        ll = [random.randint(-100, 100) for i in range(8)]
        print(f"ll is {ll}")
        c = sorted(ll.copy())
        merge_sort(ll)
        if ll != c:
            print("Found mismatch")
            print(f"expect: {c}")
            print(f"but: {ll}")
