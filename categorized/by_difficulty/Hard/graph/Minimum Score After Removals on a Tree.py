# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=3IomMslYOOY
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/minimum-score-after-removals-on-a-tree

from typing import List
from collections import defaultdict


# Approach - Using DFS
# T.C : O(n^2)
# S.C : O(V+E), V = number of vertices and E = number of edges
class Solution:
    def dfs(self, node: int, parent: int, subtreeXor: List[int], inTime: List[int], outTime: List[int],
            timer: List[int], nums: List[int], adj) -> None:
        # timer is a 1-element list to simulate C++ pass-by-reference (int &timer)
        subtreeXor[node] = nums[node]
        inTime[node] = timer[0]
        timer[0] += 1
        for ngbr in adj[node]:
            if ngbr != parent:
                self.dfs(ngbr, node, subtreeXor, inTime, outTime, timer, nums, adj)
                subtreeXor[node] ^= subtreeXor[ngbr]
        outTime[node] = timer[0]
        timer[0] += 1

    def isAncestor(self, u: int, v: int, inTime: List[int], outTime: List[int]) -> bool:
        return inTime[v] >= inTime[u] and outTime[v] <= outTime[u]

    def getScore(self, a: int, b: int, c: int) -> int:
        maxXor = max(a, b, c)
        minXor = min(a, b, c)

        return maxXor - minXor

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)  # Total number of nodes

        adj = defaultdict(list)  # adjacency list
        for edge in edges:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)

        subtreeXor = [0] * n

        inTime = [0] * n
        outTime = [0] * n

        timer = [0]

        # root = 0
        self.dfs(0, -1, subtreeXor, inTime, outTime, timer, nums, adj)

        result = float('inf')
        for u in range(1, n):
            for v in range(u + 1, n):
                if self.isAncestor(u, v, inTime, outTime):
                    xor1 = subtreeXor[v]
                    xor2 = subtreeXor[u] ^ subtreeXor[v]
                    xor3 = subtreeXor[0] ^ xor1 ^ xor2
                elif self.isAncestor(v, u, inTime, outTime):
                    xor1 = subtreeXor[u]
                    xor2 = subtreeXor[v] ^ subtreeXor[u]
                    xor3 = subtreeXor[0] ^ xor1 ^ xor2
                else:
                    xor1 = subtreeXor[u]
                    xor2 = subtreeXor[v]
                    xor3 = subtreeXor[0] ^ xor1 ^ xor2

                result = min(result, self.getScore(xor1, xor2, xor3))

        return result


Approach1 = Solution

# (Java section of the original file skipped: duplicate of the C++ approach)

if __name__ == "__main__":
    assert Solution().minimumScore([1, 5, 5, 4, 11], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 9
    assert Solution().minimumScore([5, 5, 2, 4, 4, 2], [[0, 1], [1, 2], [5, 2], [4, 3], [1, 3]]) == 0
    print("ok")
