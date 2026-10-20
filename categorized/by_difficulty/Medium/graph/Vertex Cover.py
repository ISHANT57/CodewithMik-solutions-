# MY YOUTUBE VIDEO ON THIS Qn :
# Company Tags                : Not sure if anyone will ask this :-)
# GfG Link                    : https://www.geeksforgeeks.org/problems/vertex-cover/1

# Study about Gosper's Hack - http://programmingforinsomniacs.blogspot.com/2018/03/gospers-hack-explained.html

# ************************************************************************** C++ -> Python **************************************************************************
# T.C : O(log N * 2^N * N^2),
# S.C : O(N*N)
from typing import List, Tuple


class Solution:

    def __init__(self):
        self.totalEdges = 0

    def isValidCover(self, k: int, n: int, adj: List[List[int]]) -> bool:

        set_ = (1 << k) - 1  # 'set' renamed to avoid shadowing the builtin
        limit = (1 << n)

        while set_ < limit:

            visited = [[False] * (n + 1) for _ in range(n + 1)]  # memset(visited, 0, ...)

            # ************ Main Logic Starts************
            count = 0
            j = 1
            u = 1
            while u < n + 1:
                if set_ & j:
                    for v in range(1, n + 1):

                        if adj[u][v] == 1 and not visited[u][v]:
                            visited[u][v] = True
                            visited[v][u] = True
                            count += 1
                j = j << 1
                u += 1

            if count == self.totalEdges:
                return True
            # ************ Main Logic Ends************

            c = set_ & -set_
            r = set_ + c
            set_ = (((r ^ set_) >> 2) // c) | r

        return False

    def vertexCover(self, n: int, edges: List[Tuple[int, int]]) -> int:
        self.totalEdges = len(edges)

        adj = [[0] * (n + 1) for _ in range(n + 1)]

        for it in edges:
            u = it[0]
            v = it[1]

            adj[u][v] = 1
            adj[v][u] = 1

        low, high = 1, n  # binary search
        result = n
        while low <= high:
            mid = (low + high) >> 1
            if self.isValidCover(mid, n, adj):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result


Approach1 = Solution

if __name__ == "__main__":
    # star graph: vertex 1 covers all edges
    assert Solution().vertexCover(4, [(1, 2), (1, 3), (1, 4)]) == 1
    # triangle needs 2
    assert Solution().vertexCover(3, [(1, 2), (2, 3), (1, 3)]) == 2
    print("ok")
