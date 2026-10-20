# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=8S5jpVM3kWw
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

from typing import List


########################################## Python (converted from C++) ##########################################
# Using DSU
# T.C : O(m log m) - sorting edges
#       O(m * α(n)) union-find operations takes O(α(n)) time.The loop over all edges takes O(m) time, with each find and union operation inside the loop taking O(α(n)) time.
# S.C : O(n)
class DSU:
    def __init__(self, n: int):
        self.parent = [0] * (n + 1)
        self.rank = [0] * (n + 1)
        self.components = n
        for i in range(1, n + 1):
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
        self.components -= 1

    def isSingle(self) -> bool:
        return self.components == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        # sort by type descending (v1[0] > v2[0]); key=-type gives the same ordering
        edges.sort(key=lambda v: -v[0])
        Alice = DSU(n)
        Bob = DSU(n)

        addedEdge = 0

        for edge in edges:  # For each edge -
            type = edge[0]
            u = edge[1]
            v = edge[2]

            if type == 3:
                add = False

                if Alice.find(u) != Alice.find(v):
                    Alice.Union(u, v)
                    add = True

                if Bob.find(u) != Bob.find(v):
                    Bob.Union(u, v)
                    add = True

                if add:
                    addedEdge += 1

            elif type == 2:
                if Bob.find(u) != Bob.find(v):
                    Bob.Union(u, v)
                    addedEdge += 1
            else:
                if Alice.find(u) != Alice.find(v):
                    Alice.Union(u, v)
                    addedEdge += 1

        if Alice.isSingle() and Bob.isSingle():
            return len(edges) - addedEdge

        return -1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]) == 2
    assert Solution().maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]) == 0
    assert Solution().maxNumEdgesToRemove(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]) == -1
    print("ok")
