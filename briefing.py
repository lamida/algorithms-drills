# The example of problem on the interview briefing call
"""
Array duplicates
"""
from typing import List
def duplicate(array: List[int]):
    cache = {}
    for i in array:
        if cache.get(i) is None:
            return True
    return False

if __name__ == "__main__":
    res = duplicate([1,1,2,3])
    print(res)
