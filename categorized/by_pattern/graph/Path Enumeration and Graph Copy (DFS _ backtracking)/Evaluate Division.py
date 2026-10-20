#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=C6cm6IvqmyA
#     Company Tags                : Amazon, Meta
#     Leetcode Link               : https://leetcode.com/problems/evaluate-division/

import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(10000)


class Solution:

    # ans is passed by reference in C++ (double &ans) -> one-element list here
    def dfs(self, adj, src: str, dst: str, visited: set, product: float, ans: List[float]) -> None:
        if src in visited:
            return

        visited.add(src)
        if src == dst:
            ans[0] = product
            return

        for p in adj[src]:

            v = p[0]
            val = p[1]

            self.dfs(adj, v, dst, visited, product * val, ans)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)

        adj = defaultdict(list)

        for i in range(n):

            u = equations[i][0]
            v = equations[i][1]
            val = values[i]

            adj[u].append((v, val))        # To handle a/c
            adj[v].append((u, 1.0 / val))  # To handle c/a

        result = []

        for query in queries:

            src = query[0]
            dst = query[1]

            ans = [-1.0]
            product = 1.0

            if src in adj:
                visited = set()

                self.dfs(adj, src, dst, visited, product, ans)

            result.append(ans[0])

        return result


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    r = s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                       [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    assert all(abs(x - y) < 1e-5 for x, y in zip(r, [6.0, 0.5, -1.0, 1.0, -1.0])), r
    print("ok")
