# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=7wGJ1nevpnc
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [False] * n

        for edge in edges:

            u = edge[0]
            v = edge[1]

            indegree[v] = True

        result = []

        for i in range(n):
            if indegree[i] == False:
                result.append(i)

        return result

Approach1 = Solution


if __name__ == "__main__":
    assert Solution().findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]) == [0,3]
    assert Solution().findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]) == [0,2,3]
    print("ok")
