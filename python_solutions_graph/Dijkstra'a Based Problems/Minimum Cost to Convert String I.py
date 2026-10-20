#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=M8WnAIhTjmQ
#     Company Tags                : will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-cost-to-convert-string-i/

from typing import List
from collections import defaultdict
import heapq

INT_MAX = 2**31 - 1

# Approach-1 (Using Simple Dijkstra's Algorithm)
# T.C : n * (time complexity of Dijkstra) = O(n * (V+E)logV) , where V = number of vertices and E = number of edges
# S.C : O(V+E) -> We create a graph, where V = number of vertices and E = number of edges
class Solution:
    def dijkstra(self, source: str, adj, costMatrix: List[List[int]]) -> None:

        # min-heap
        pq = []

        heapq.heappush(pq, (0, source))

        while pq:
            d, adjNode = heapq.heappop(pq)

            for it in adj[adjNode]:
                adjNode2 = it[0]  # shadows adjNode in the C++ inner loop
                cost     = it[1]

                if costMatrix[ord(source) - ord('a')][ord(adjNode2) - ord('a')] > d + cost:
                    costMatrix[ord(source) - ord('a')][ord(adjNode2) - ord('a')] = d + cost
                    heapq.heappush(pq, (d + cost, adjNode2))
        return

    # V = # of vertices
    # E = # of edges
    # O(n * (V+E)log(V))
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)

        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))

        costMatrix = [[INT_MAX] * 26 for _ in range(26)]

        # Populate the costMatrix using Dijkstra's Algorithm
        for i in range(len(source)):  # n
            ch = source[i]
            self.dijkstra(ch, adj, costMatrix)

        ans = 0

        for i in range(len(source)):
            if source[i] == target[i]:
                continue

            if costMatrix[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == INT_MAX:
                return -1

            ans += costMatrix[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]

        return ans

Approach1 = Solution


# Approach-2 (Simply replace Dijkstra's with Floyd Warshall)
# Link (Inside my "Floyd Warshall" folder) - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Floyd%20Warshall/Minimum%20Cost%20to%20Convert%20String%20I.cpp


if __name__ == "__main__":
    s = Solution()
    assert s.minimumCost("abcd", "acbe", list("abcced"), list("bcbebe"), [2, 5, 5, 1, 2, 20]) == 28
    assert s.minimumCost("aaaa", "bbbb", ["a", "c"], ["c", "b"], [1, 2]) == 12
    assert s.minimumCost("abcd", "abce", ["a"], ["e"], [10000]) == -1
    print("ok")
