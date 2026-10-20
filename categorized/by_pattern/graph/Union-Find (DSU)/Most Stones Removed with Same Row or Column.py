# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=cmqIeBFx01w
# Company Tags                : Google
# Leetcode Link               : https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
#
# Please see the "DFS" solution : https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/BFS_DFS/Most%20Stones%20Removed%20with%20Same%20Row%20or%20Column.cpp

from typing import List


########################################## Python (converted from C++) ##########################################
# T.C : O(n^2 * α(n))
# S.C : O(n)
class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []
        self.n = 0

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])

        return self.parent[i]

    def Union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i

    def removeStones(self, stones: List[List[int]]) -> int:
        n = self.n = len(stones)
        self.parent = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.Union(i, j)

        groups = 0
        for i in range(n):
            if self.parent[i] == i:
                groups += 1

        return n - groups


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
    assert Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3
    assert Solution().removeStones([[0, 0]]) == 0
    print("ok")
