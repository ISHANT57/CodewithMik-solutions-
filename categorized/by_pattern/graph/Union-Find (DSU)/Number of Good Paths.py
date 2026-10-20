# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Y02Muq_xoCg
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/number-of-good-paths/submissions/

from typing import List
from collections import defaultdict


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

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)

        self.parent = [0] * n
        self.rank = [1] * n

        for i in range(n):
            self.parent[i] = i

        adj = defaultdict(list)

        for vec in edges:
            u = vec[0]
            v = vec[1]

            adj[u].append(v)
            adj[v].append(u)

        # map<int, vector<int>> is ordered by key -> dict, iterated in sorted key order below
        val_to_nodes = defaultdict(list)

        for i in range(n):
            value = vals[i]

            val_to_nodes[value].append(i)

        result = n

        is_active = [False] * n  # non active in the beginning

        for key in sorted(val_to_nodes):
            nodes = list(val_to_nodes[key])

            for u in nodes:

                for v in adj[u]:
                    if is_active[v]:
                        self.Union(u, v)
                is_active[u] = True

            tumhare_parents = []

            for u in nodes:
                tumhare_parents.append(self.find(u))

            tumhare_parents.sort()

            sz = len(tumhare_parents)

            j = 0
            while j < sz:
                count = 0

                cur_parent = tumhare_parents[j]

                while j < sz and tumhare_parents[j] == cur_parent:
                    j += 1
                    count += 1
                j -= 1

                result += (count * (count - 1)) // 2
                j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().numberOfGoodPaths([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]) == 6
    assert Solution().numberOfGoodPaths([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]) == 7
    assert Solution().numberOfGoodPaths([1], []) == 1
    print("ok")
