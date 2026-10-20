# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Hh_9ppxgzpo
# Company Tags                : MICROSOFT
# Leetcode Link               : https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
#
# NOTE : DFS and BFS Approach already shared here (below link) :
# https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/BFS_DFS/Count%20Unreachable%20Pairs%20of%20Nodes%20in%20an%20Undirected%20Graph.cpp

from typing import List
from collections import defaultdict


# DSU : Time complexity: O(V+E) ,  Here 'V' is the number of nodes and 'E' is the total number edges.
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

    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        self.parent = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.parent[i] = i

        for vec in edges:

            u = vec[0]
            v = vec[1]

            self.Union(u, v)

        mp = defaultdict(int)

        for i in range(n):
            papa = self.find(i)
            mp[papa] += 1

        result = 0
        remainingNodes = n

        for it in mp.items():

            size = it[1]

            result += (size) * (remainingNodes - size)

            remainingNodes -= size

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().countPairs(3, [[0, 1], [0, 2], [1, 2]]) == 0
    assert Solution().countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14
    print("ok")
