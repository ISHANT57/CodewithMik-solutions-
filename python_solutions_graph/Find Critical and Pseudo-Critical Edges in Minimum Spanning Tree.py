#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=gDPh7gsK3F8
#       Company Tags                : Amazon, Meta
#       Leetcode Link               : https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

import sys
from typing import List

sys.setrecursionlimit(10000)

INT_MAX = 2**31 - 1


# ***************************************** C++ *****************************************
# Using Union Find + Kruskal's. T.C : ElogE + E*@ + E*E*@ - Explained in the video above
class Solution:
    class UnionFind:
        def __init__(self, n: int):
            self.parent = [0] * n
            self.rank = [0] * n
            for i in range(n):
                self.parent[i] = i

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

    def Kruskal(self, vec: List[List[int]], skip_edge: int, force_edge: int) -> int:

        sum_ = 0
        uf = Solution.UnionFind(self.N)

        if force_edge != -1:
            uf.Union(vec[force_edge][0], vec[force_edge][1])
            sum_ += vec[force_edge][2]

        for i in range(len(vec)):

            if i == skip_edge:
                continue

            u = vec[i][0]
            v = vec[i][1]
            wt = vec[i][2]

            parent_u = uf.find(u)
            parent_v = uf.find(v)

            if parent_u != parent_v:
                uf.Union(u, v)
                sum_ += wt

        # Check if all vertices are included in MST
        for i in range(self.N):
            if uf.find(i) != uf.find(0):
                return INT_MAX

        return sum_

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.N = n

        # since for kruskal's algo, we will sort our input by edge weight.
        # But since we need to return the index in the last
        for i in range(len(edges)):
            edges[i].append(i)

        # Now sort based on weight
        # O(ElogE)
        edges.sort(key=lambda v: v[2])

        # Find MST now
        # Find MST weight using union-find
        # O(E*@)
        MST_WEIGHT = self.Kruskal(edges, -1, -1)

        critical = []
        pseudo_critical = []

        # O(E*E*@)
        for i in range(len(edges)):

            if self.Kruskal(edges, i, -1) > MST_WEIGHT:  # Skipping ith edge
                critical.append(edges[i][3])

            elif self.Kruskal(edges, -1, i) == MST_WEIGHT:  # Force add ith edge
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]


Approach1 = Solution


# Approach-2 (Better Kruskal's Function)
"""
If you remember, in the Kruskal's Function, in the end we checked if the graph was connected and wrote a for loop to check that as shown below :
for(int i = 0; i<N; i++) {
            if(uf.find(i) != uf.find(0))
                return INT_MAX;
 }

BUT BUT BUT, we can also directly check if the total edges we made from Union is equal to (V-1).
Remember, in MST, there must be V vertices and must have (V-1) edges.
So, in Kruskal's function, whenever you do Union, just count the edges you draw.

So, simply replace the for loop with :
if(edgesConnected != N-1)
            return INT_MAX;

Full code below :
"""
class Solution:
    class UnionFind:
        def __init__(self, n: int):
            self.parent = [0] * n
            self.rank = [0] * n
            for i in range(n):
                self.parent[i] = i

        def find(self, x: int) -> int:
            if x == self.parent[x]:
                return x

            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def Union(self, x: int, y: int) -> bool:
            x_parent = self.find(x)
            y_parent = self.find(y)

            if x_parent == y_parent:
                return False

            if self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            elif self.rank[x_parent] < self.rank[y_parent]:
                self.parent[x_parent] = y_parent
            else:
                self.parent[x_parent] = y_parent
                self.rank[y_parent] += 1
            return True

    def Kruskal(self, vec: List[List[int]], skip_edge: int, add_edge: int) -> int:

        sum_ = 0

        uf = Solution.UnionFind(self.N)
        edgesConnected = 0

        if add_edge != -1:
            uf.Union(vec[add_edge][0], vec[add_edge][1])
            sum_ += vec[add_edge][2]
            edgesConnected += 1

        # E

        for i in range(len(vec)):

            if i == skip_edge:
                continue

            u = vec[i][0]
            v = vec[i][1]
            wt = vec[i][2]
            # O(@)
            parent_u = uf.find(u)
            parent_v = uf.find(v)

            if parent_u != parent_v:
                uf.Union(u, v)
                edgesConnected += 1
                sum_ += wt

        if edgesConnected != self.N - 1:
            return INT_MAX

        return sum_

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.N = n
        for i in range(len(edges)):
            edges[i].append(i)

        # ElogE
        edges.sort(key=lambda vec: vec[2])

        MST_WEIGHT = self.Kruskal(edges, -1, -1)

        critical = []
        pseudo_critical = []

        # E*E*@
        for i in range(len(edges)):

            if self.Kruskal(edges, i, -1) > MST_WEIGHT:  # skipping ith edge
                critical.append(edges[i][3])

            elif self.Kruskal(edges, -1, i) == MST_WEIGHT:  # Force add this ith edge
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        r = S().findCriticalAndPseudoCriticalEdges(
            5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]])
        assert sorted(r[0]) == [0, 1] and sorted(r[1]) == [2, 3, 4, 5], r
        r = S().findCriticalAndPseudoCriticalEdges(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]])
        assert r[0] == [] and sorted(r[1]) == [0, 1, 2, 3], r
    print("ok")
