# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Xw6lpWDh82E
# Company Tags                : AMAZON
# Leetcode Link               : https://leetcode.com/problems/similar-string-groups/

# NOTE : Find my BFS and DFS approach in below link (in my Graph/BFS_DFS repo
# Link : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/BFS_DFS/Similar%20String%20Groups.cpp

from typing import List


# Approach : Using DSU
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

    def isSimilar(self, s1: str, s2: str) -> bool:

        n = len(s1)
        diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1

        return diff == 2 or diff == 0

    def numSimilarGroups(self, strs: List[str]) -> int:

        n = len(strs)
        self.parent = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.parent[i] = i

        groups = n  # Initially all strings represent themselves

        for i in range(n):
            for j in range(i + 1, n):

                if self.isSimilar(strs[i], strs[j]) and self.find(i) != self.find(j):
                    groups -= 1
                    self.Union(i, j)

        return groups


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().numSimilarGroups(["tars", "rats", "arts", "star"]) == 2
    assert Solution().numSimilarGroups(["omv", "ovm"]) == 1
    print("ok")
