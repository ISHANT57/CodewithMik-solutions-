#     Scroll below to see JAVA code also
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=wiJaMH1CMhw
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimum-cost-to-convert-string-ii

import sys
from typing import List
from collections import defaultdict
import heapq

sys.setrecursionlimit(20000)

# Approach (Using Dijkstra's Algorithm and DP with Power of Memoization for both)
#
# N = length of sourceStr / targetStr
# M = number of conversion rules (original.size())
# L = number of distinct substring lengths
# (L = lengthSet.size())
# V = number of unique strings appearing in original and changed
# E = number of edges in graph (E = M)
# T.C : O(
#           M                           // graph build
#           + M log L                     // lengthSet
#           + N^2 x L                      // DP overhead
#           + M^2 x (V + E) log V          // Dijkstra
#         )
#   S.C : O(M^2 + V + E + N)
class Solution:
    def __init__(self):
        self.BIG_VALUE = int(1e10)
        self.adj = defaultdict(list)  # Graph

        # start -> end -> anser
        self.dijkstraMemo = defaultdict(dict)

        self.dpMemo = []

        self.sourceStr = ""
        self.targetStr = ""
        # set<int> in C++ iterates in sorted order; here a set that is iterated via sorted()
        self.validLengths = set()

    def dijkstra(self, start: str, end: str) -> int:

        if end in self.dijkstraMemo[start]:
            return self.dijkstraMemo[start][end]

        # {cost, string}
        pq = []  # min-heap
        # vector<int> result(n, INT_MAX)
        result = {}  # source to string ka cost stored
        result[start] = 0
        heapq.heappush(pq, (0, start))

        while pq:
            currCost, node = heapq.heappop(pq)

            if node == end:
                break

            for adjNode, edgeCost in self.adj[node]:
                if adjNode not in result or currCost + edgeCost < result[adjNode]:
                    result[adjNode] = currCost + edgeCost
                    heapq.heappush(pq, (currCost + edgeCost, adjNode))

        finalCost = result[end] if end in result else self.BIG_VALUE

        self.dijkstraMemo[start][end] = finalCost
        return finalCost

    def solve(self, idx: int) -> int:
        if idx >= len(self.sourceStr):
            return 0
        if self.dpMemo[idx] != -1:
            return self.dpMemo[idx]

        minCost = self.BIG_VALUE

        if self.sourceStr[idx] == self.targetStr[idx]:
            minCost = self.solve(idx+1)

        for length in sorted(self.validLengths):
            if idx + length > len(self.sourceStr):
                break

            srcSub = self.sourceStr[idx:idx+length]
            tgtSub = self.targetStr[idx:idx+length]

            if srcSub not in self.adj:
                continue

            minPathCost = self.dijkstra(srcSub, tgtSub)
            if minPathCost == self.BIG_VALUE:
                continue

            minCost = min(minCost, minPathCost + self.solve(idx+length))

        self.dpMemo[idx] = minCost
        return minCost

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        self.sourceStr = source
        self.targetStr = target

        self.dpMemo = [-1] * 10001

        for i in range(len(original)):
            self.adj[original[i]].append((changed[i], cost[i]))

        for s in original:
            self.validLengths.add(len(s))

        result = self.solve(0)

        return -1 if result == self.BIG_VALUE else result

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumCost("abcd", "acbe", ["a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]) == 28
    assert Solution().minimumCost("abcdefgh", "acdeeghh", ["bcd", "fgh", "thh"], ["cde", "thh", "ghh"], [1, 3, 5]) == 9
    assert Solution().minimumCost("abcdefgh", "addddddd", ["bcd", "defgh"], ["ddd", "ddddd"], [100, 1578]) == -1
    print("ok")
