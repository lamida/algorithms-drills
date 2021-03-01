import heapq
import functools
from typing import List

def findMaxProduct(arr: List[int]) -> List[int]:
    output = [-1] * len(arr)
    h = []

    heapq.heappush(h, arr[0])
    heapq.heappush(h, arr[1])
    for i in range(2, len(arr)):
        heapq.heappush(h, arr[i])
        output[i] = functools.reduce(lambda a, b: a * b, heapq.nlargest(3, h))
    return output

if __name__ == "__main__":
    n = 5
    arr = [1,2,3,4,5]
    output = findMaxProduct(arr)
    print(output)