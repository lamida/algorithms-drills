import heapq
from typing import List
def findMedian(arr: List[int]) -> List[int]:
    output = [None] * len(arr)
    output[0] = arr[0]

    h = []
    heapq.heappush(h, arr[0])
    for i in range(1, len(arr)):
        heapq.heappush(h, arr[i])
        idx = i + 1
        if idx % 2 == 0:
            mid = idx//2
            left = heapq.nsmallest(mid, h)[-1]
            right = heapq.nlargest(mid, h)[-1]
            output[i] = int((left + right)//2)
        else:
            mid = 1 + idx // 2
            output[i] = heapq.nsmallest(mid, h)[-1]
    return output

if __name__ == "__main__":
    arr = [5, 15, 1, 3]
    output = findMedian(arr)
    print(output)