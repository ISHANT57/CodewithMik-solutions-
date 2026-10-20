# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=BZ-dn_2oupQ
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades

from typing import List


############################################ Python (converted from C++) ############################################
# Approach - (Binary Search + DSU)
# T.C : O(nlog(maxStability - minStability))
# S.C : O(n+e), n = number of nodes, e = number of edges
class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

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


class Solution:

    def check(self, n: int, edges: List[List[int]], k: int, mid: int) -> bool:
        dsu = DSU(n)

        upgradeCandidates = []

        for edge in edges:  # E
            u = edge[0]
            v = edge[1]

            s = edge[2]
            m = edge[3]

            if m == 1:
                if s < mid:
                    return False

                dsu.Union(u, v)  # alpa
            else:
                if s >= mid:
                    # no need to upgrade
                    dsu.Union(u, v)
                elif 2 * s >= mid:
                    upgradeCandidates.append([u, v])

        for edge in upgradeCandidates:  # O(E)
            u = edge[0]
            v = edge[1]

            if dsu.find(u) != dsu.find(v):
                if k <= 0:
                    return False

                dsu.Union(u, v)
                k -= 1  # upgrade

        root = dsu.find(0)
        for node in range(1, n):  # O(n)
            if dsu.find(node) != root:
                return False
        return True

    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        """
            Input: n = 3, edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]], k = 0
            0 --- 1 --- 2 , parent = 0
            (2, 0)
            2 ka. parent kaun hai = 0
            0 ka parent kaun hai  = 0
        """

        dsu = DSU(n)
        for edge in edges:
            u = edge[0]
            v = edge[1]

            s = edge[2]
            m = edge[3]

            if m == 1:  # must be included in the spanning tree
                if dsu.find(u) == dsu.find(v):
                    return -1

                dsu.Union(u, v)

        result = -1
        l = 1
        r = int(2 * 1e5)

        # T.C : O(nlogn)
        while l <= r:
            mid = l + (r - l) // 2

            if self.check(n, edges, k, mid):
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxStability(3, [[0, 1, 2, 1], [1, 2, 3, 0]], 1) == 2
    assert Solution().maxStability(3, [[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], 2) == 6
    assert Solution().maxStability(3, [[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]], 0) == -1
    print("ok")
