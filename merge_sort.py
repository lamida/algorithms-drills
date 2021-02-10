# This is ridiculous, but I am still loss in merge sort :(
from typing import List

def merge(arr: List[int]):
    mid = len(arr)//2
    i = 0 
    j = mid + 1

    aux = arr.copy()

    for k in range(len(arr)):
        if i > mid:
            arr[k] = aux[j]
            j+=1
        elif j > len(arr) - 1: # why len - 1?
            arr[k] = aux[i]
            i+=1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j+=1
        else:
            arr[k] = aux[i]
            i+=1
        
def sort(arr: List[int]):
    if len(arr) > 1:
        mid = len(arr)//2
        sort(arr[:mid])
        sort(arr[mid:])
        print(f"merging: {arr}")
        merge(arr)
        print(f"merged: {arr}")

import random
if __name__ == "__main__":
    # ll = [-30, 13, -43, -7] 
    # merge(ll)
    # print(ll)
    for ll in [[-30, 13, -43, -7, 26, -48, 94, 93]]:
        print(f"ll is {ll}")
        c = sorted(ll.copy())
        sort(ll)
        if ll != c:
            print("Found mismatch")
            print(f"expect: {c}")
            print(f"but: {ll}")
    # for i in range(10):
    #     ll = [random.randint(-100, 100) for i in range(8)]
    #     print(f"ll is {ll}")
    #     c = sorted(ll.copy())
    #     sort(ll)
    #     if ll != c:
    #         print("Found mismatch")
    #         print(f"expect: {c}")
    #         print(f"but: {ll}")

