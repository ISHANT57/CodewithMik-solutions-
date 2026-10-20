# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=q2xBd-D_1KQ
# Company Tags                : AMAZON
# Leetcode Link               : https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from typing import List


class Solution:

    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        self.parent = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.parent[i] = i

        components = n
        for vec in connections:
            if self.find(vec[0]) != self.find(vec[1]):
                components -= 1
                self.Union(vec[0], vec[1])
        return components - 1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().makeConnected(4, [[0, 1], [0, 2], [1, 2]]) == 1
    assert Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]) == 2
    assert Solution().makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]) == -1
    print("ok")
