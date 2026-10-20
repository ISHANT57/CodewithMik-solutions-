# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=M8WnAIhTjmQ
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/minimum-cost-to-convert-string-i/

from typing import List

# Approach-1 (Using Simple Floyd Warshall Algorithm)
# T.C : O(n)  -> Because other for loops run only for constant time 26*26*26
# S.C : O(1) -> We take distances matrix of 26*26 which is constant
class Solution:

    def FloydWarshall(self, adjMatrix: List[List[int]], original: List[str], changed: List[str], cost: List[int]) -> None:

        for i in range(len(original)):
            s = ord(original[i]) - ord('a')
            t = ord(changed[i]) - ord('a')

            adjMatrix[s][t] = min(adjMatrix[s][t], cost[i])

        # Apply Floyd Warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INT_MAX = 2**31 - 1
        adjMatrix = [[INT_MAX] * 26 for _ in range(26)]

        self.FloydWarshall(adjMatrix, original, changed, cost)  # update adjMatrix with shortest path using Floyd Warshall

        ans = 0

        for i in range(len(source)):
            if source[i] == target[i]:
                continue

            if adjMatrix[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == INT_MAX:
                return -1

            ans += adjMatrix[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]

        return ans

Approach1 = Solution

# Approach-2 (Simply replace Floyd Warshall with Dijkstra's Algorithm)
# Link (Inside my "Dijkstra's Based Problems" Warshall folder) - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Graph/Dijkstra'a%20Based%20Problems/Minimum%20Cost%20to%20Convert%20String%20I.cpp


if __name__ == "__main__":
    assert Solution().minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]) == 28
    assert Solution().minimumCost("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]) == 12
    assert Solution().minimumCost("abcd", "abce", ["a"], ["e"], [10000]) == -1
    print("ok")
