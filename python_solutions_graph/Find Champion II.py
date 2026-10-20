#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=1tsmqSn-O_0
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/find-champion-ii

from typing import List


# ************************************************************ C++ ************************************************
# Approach - Simple indegree check
# T.C : O(m + n)
# S.C : O(n)
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for edge in edges:
            u = edge[0]
            v = edge[1]

            # u --> v
            indegree[v] += 1

        champ = -1
        count = 0
        for i in range(n):
            if indegree[i] == 0:  # ith node is the champion
                champ = i
                count += 1
                if count > 1:
                    return -1

        return champ


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    assert s.findChampion(3, [[0, 1], [1, 2]]) == 0
    assert s.findChampion(4, [[0, 2], [1, 3], [1, 2]]) == -1
    print("ok")
