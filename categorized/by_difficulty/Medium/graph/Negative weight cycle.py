# MY YOUTUBE VIDEO ON THIS Qn : <soon>
# Company Tags                : Amazon, Microsoft, Cisco (Generally asked as a follow up qn of Dijkstra's Algorithm)
# GfG Link                    : https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1

from typing import List


class Solution:
    def isNegativeWeightCycle(self, n: int, edges: List[List[int]]) -> int:
        result = [10 ** 8] * n  # 1e8

        for c in range(1, n + 1):

            for edge in edges:

                u = edge[0]
                v = edge[1]
                w = edge[2]

                if result[u] + w < result[v]:
                    if c == n:
                        return 1
                    result[v] = result[u] + w

        return 0


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().isNegativeWeightCycle(3, [[0, 1, -1], [1, 2, -2], [2, 0, -3]]) == 1
    assert Solution().isNegativeWeightCycle(3, [[0, 1, -1], [1, 2, -2], [0, 2, -3]]) == 0
    print("ok")
