from typing import List

"""
q[i=0..n] is the position of queen in row i.
r is the attempt to place queen in row r.
From Algorithms - Jeff Errickson
"""
def place_queen(q: List[int], r: int):
    if r == len(q):
        print(q)
    else:
        # looping columns in the row of r
        for j in range(len(q)):
            legal = True
            # looping previous rows
            for i in range(r):
                if q[i] == j or q[i] == j + r - i or q[i] == j - r + i:
                    legal = False
            if legal:
                q[r] = j
                place_queen(q, r + 1) 

if __name__ == "__main__":
    # test using 4*4 boards
    q = [0] * 4
    place_queen(q, 0)
    
