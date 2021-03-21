# Maximum sum of contagious sub array of size k
# https://www.youtube.com/watch?v=MK-NZ4hN7rs&ab_channel=TheSimpleEngineer
from typing import List
def mx(s: List[int], k: int) -> int:
    m = 0
    ss = 0
    
    # First window
    for i in range(k):
        ss += s[i]

    m = max(m, ss)
    for i in range(k, len(s)):
        r = i - k
        ss -= s[r]
        ss += s[i]
        m = max(m, ss)
    return m

if __name__ == "__main__":
    print(mx([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))
