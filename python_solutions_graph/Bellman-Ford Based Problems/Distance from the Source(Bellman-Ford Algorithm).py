# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=5yTkgeTqKK0
# Company Tags                : Amazon, Microsoft (Generally asked as a follow up qn of Dijkstra's Algorithm)
# GfG Link                    : https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

from typing import List


class Solution:
    def bellman_ford(self, V: int, edges: List[List[int]], S: int) -> List[int]:
        result = [10 ** 8] * V  # 1e8 kept as int
        result[S] = 0

        for c in range(1, V):

            for edge in edges:

                u = edge[0]
                v = edge[1]
                w = edge[2]

                if result[u] != 10 ** 8 and result[u] + w < result[v]:
                    result[v] = result[u] + w

        # Now detect negative cycle
        for edge in edges:

            u = edge[0]
            v = edge[1]
            w = edge[2]

            if result[u] != 10 ** 8 and result[u] + w < result[v]:
                return [-1]

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().bellman_ford(5, [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]], 0) == [0, 5, 6, 6, 7]
    assert Solution().bellman_ford(4, [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]], 0) == [-1]
    print("ok")
