# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=r0s0BtmTxWk
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations

from typing import List
from collections import defaultdict


############################################ Python (converted from C++) ############################################
# Approach - (DSU + map)
# T.C : O(n + m*alpha(n)), alpha(n) = inverse Ackermann function.
# S.C : O(n)
class Solution:
    # DSU using rank and path compression
    def __init__(self):
        self.rank = []
        self.parent = []

    # Find with path compression
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return

        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX

        self.parent[rootY] = rootX

        if self.rank[rootX] == self.rank[rootY]:
            self.rank[rootX] += 1

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        self.parent = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.parent[i] = i

        # Union of allowedSwaps
        for vec in allowedSwaps:  # O(m*alpha)
            self.Union(vec[0], vec[1])

        # unordered_map<int, unordered_map<int, int>> -> defaultdict of defaultdict
        groupFreq = defaultdict(lambda: defaultdict(int))

        for i in range(n):  # O(n*alpha)
            curr = source[i]

            parent = self.find(i)  # group
            groupFreq[parent][curr] += 1

        hammingDistance = 0
        for i in range(n):
            parent = self.find(i)  # group

            if groupFreq[parent][target[i]] > 0:
                groupFreq[parent][target[i]] -= 1
            else:
                hammingDistance += 1

        return hammingDistance


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumHammingDistance([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]]) == 1
    assert Solution().minimumHammingDistance([1, 2, 3, 4], [1, 3, 2, 4], []) == 2
    assert Solution().minimumHammingDistance([5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]]) == 0
    print("ok")
