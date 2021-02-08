# This is ridiculous, but I am still loss in merge sort :(
from typing import List
def merge(arr: List[int], m: int):
    aux = arr.copy()
    i = 0
    j = m
    n = len(arr) - 1
    print(f"merge. arr: {arr}, m: {m}, i: {i}, j: {j}, n: {n}")

    print(f"range: {list(range(i, n+1))}")
    for k in range(i, n + 1):
        if j > n:
            print(f"index right: {j} is larger than max: {n}, append left to index {k}")
            aux[k] = arr[i]
            i += 1
        elif i > m:
            print(f"index left: {i} is larger than mid: {m}, append right to index {k}")
            aux[k] = arr[j]
            j += 1
        if arr[i] < arr[j]:
            print(f"right: {aux[j]} is larger than left: {aux[i]}, append left to index {k}")
            aux[k] = arr[i]
            i += 1
        else:
            print(f"right: {aux[j]} is smaller than left: {aux[i]}, append right to index {k}")
            aux[k] = arr[j]
            j += 1
    
    for k in range(i, n + 1):
        arr[k] = aux[k]


def merge2(s1: List[int], s2: List[int], s: List[int]):
    i = 0
    j = 0
    while i + j < len(s):
        if j == len(s1) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i+=1
        else:
            s[i+j] = s2[j]
            j += 1

        

def sort(arr: List[int]):
    if len(arr) > 1:
        mid = len(arr)//2
        sort(arr[:mid])
        sort(arr[mid:])
        print(f"merging: {arr}")
        merge(arr, mid)

if __name__ == "__main__":
    s1 = [100]
    s2 = [10]
    s = [None] * 2
    merge2(s1, s2, s)
    print(s)
