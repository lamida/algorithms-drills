# https://leetcode.com/explore/featured/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
from typing import List

def shift(arr: List[int]):
    i = 1
    while i < len(arr):
        j = i - 1  
        c = arr[j]
        if c == 0:
            arr.insert(j, 0)
            arr.pop()
            i += 2
        i+=1

if __name__ == "__main__":
    l = [1, 0, 4]
    shift(l)
    print(l)