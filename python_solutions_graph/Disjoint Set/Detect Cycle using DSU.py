# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=0X0lEtTkk-8
# Compnay Tags                : Google, Microsoft
# GfG Link                    : https://practice.geeksforgeeks.org/problems/detect-cycle-using-dsu/1

from typing import List


class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

    # Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V: int, adj: List[List[int]]) -> int:
        self.parent = [0] * V
        self.rank = [0] * V

        for i in range(V):
            self.parent[i] = i

        for u in range(V):
            for v in adj[u]:
                if u < v:
                    if self.find(u) == self.find(v):
                        return True
                    else:
                        self.Union(u, v)
        return False


Approach1 = Solution


if __name__ == "__main__":
    # cycle 0-1-2-0
    assert Solution().detectCycle(3, [[1, 2], [0, 2], [0, 1]]) == True
    # tree 0-1, 1-2
    assert Solution().detectCycle(3, [[1], [0, 2], [1]]) == False
    print("ok")
