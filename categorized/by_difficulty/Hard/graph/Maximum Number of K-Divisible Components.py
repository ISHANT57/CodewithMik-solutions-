# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=RnFCrjkkIUE
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/maximum-number-of-k-divisible-components

from typing import List
from collections import defaultdict


# ****************************************************************** C++ ******************************************************************
# Approach (Using DFS) - You can easily replace DFS with BFS as well
# T.C : O(n) - We visit all nodes once
# S.C : O(n-1) ~ O(n) - We store edges in the adjacency list
class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, curr: int, parent: int, adj, values: List[int], k: int) -> int:

        sum = 0

        for ngbr in adj[curr]:
            if ngbr != parent:
                sum += self.dfs(ngbr, curr, adj, values, k)
                sum %= k

        sum += values[curr]
        sum %= k

        if sum == 0:
            self.count += 1

        return sum

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        adj = defaultdict(list)  # unordered_map<int, vector<int>>
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        self.count = 0

        self.dfs(0, -1, adj, values, k)

        return self.count


Approach1 = Solution

# (The Java section of the original file duplicates the above and is skipped.)


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**6)
    assert Solution().maxKDivisibleComponents(5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6) == 2
    assert Solution().maxKDivisibleComponents(7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3) == 3
    print("ok")
