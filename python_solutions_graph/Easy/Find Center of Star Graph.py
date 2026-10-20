#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Sp9kcIX0Ep0
#     Company Tags                : MICROSOFT
#     Leetcode Link               : https://leetcode.com/problems/find-center-of-star-graph

from collections import defaultdict
from typing import List


# ************************************************************************ C++ ********************************************************
# Approach-1 (Using map)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        degree = defaultdict(int)

        for vec in edges:
            u = vec[0]
            v = vec[1]

            degree[u] += 1
            degree[v] += 1

        for node, deg in degree.items():
            if deg == n:
                return node

        return -1


Approach1 = Solution


# Approach-2 (Constant time)
# T.C : O(1)
# S.C : O(1)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0]   # {a, b}
        second = edges[1]  # {c, a}

        if first[0] == second[0] or first[0] == second[1]:
            return first[0]

        return first[1]


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        s = S()
        assert s.findCenter([[1, 2], [2, 3], [4, 2]]) == 2
        assert s.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
    print("ok")
