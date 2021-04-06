class DisjoinSets:
    def __init__(self):
        self.s = [-1] * 8
        self.distance = [-1] * 8

    def find(self, i: int) -> int:
        return i if self.s[i] < 0 else self.find(self.s[i])

    def union(self, i: int, j: int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.s[root_i] = root_j
        
if __name__ == "__main__":
    edges = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,6], [6,7], [7,3]]
    ds = DisjoinSets()
    for edge in edges:
        ds.union(edge[0], edge[1])

    for i in range(8):
        print(i, ds.find(i))
