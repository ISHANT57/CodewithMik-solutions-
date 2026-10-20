# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=b6DrMMHFiL0
# Company Tags                : Google
# Leetcode Link               : https://leetcode.com/problems/sum-of-distances-in-tree/

import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(100000)


# Time : O(n), Space : O(n)
class Solution:
    def __init__(self):
        # store count of subtrees of each node
        self.result_base_node = 0
        self.count = []
        self.N = 0

    def dfsBase(self, adj, curr_node: int, prev_node: int, curr_depth: int) -> int:
        total_node = 1

        self.result_base_node += curr_depth

        for child in adj[curr_node]:
            if child == prev_node:
                continue

            total_node += self.dfsBase(adj, child, curr_node, curr_depth + 1)

        # store count of subtrees of each node
        self.count[curr_node] = total_node

        return total_node

    def DFS(self, adj, parent_node: int, prev_node: int, result: List[int]):

        for child in adj[parent_node]:
            if child == prev_node:
                continue

            result[child] = result[parent_node] - self.count[child] + (self.N - self.count[child])
            self.DFS(adj, child, parent_node, result)

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        self.N = n
        self.count = [0] * n
        for vec in edges:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        self.result_base_node = 0

        self.dfsBase(adj, 0, -1, 0)

        result = [0] * n

        result[0] = self.result_base_node

        self.DFS(adj, 0, -1, result)

        return result


Approach1 = Solution

if __name__ == "__main__":
    res = Solution().sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]])
    print(res)
    assert res == [8, 12, 6, 10, 10, 10]
    assert Solution().sumOfDistancesInTree(1, []) == [0]
    print("ok")
