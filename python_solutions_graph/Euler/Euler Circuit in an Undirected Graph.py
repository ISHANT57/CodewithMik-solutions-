#     MY YOUTUBE VIDEO ON THIS Qn : https://youtu.be/CeO0JEX4QAc?si=lb-UpnVKDMZgr4-8 (Theory video - Just use the theory and this problem will be super easy)
#     Company Tags                : Will update soon.
#     GfG Link                    : https://www.geeksforgeeks.org/problems/euler-circuit-in-a-directed-graph/1

from typing import List


# ******************************************************** C++ ****************************************************************
# T.C : O(V)
# S.C : O(1)
class Solution:
    def isEularCircuitExist(self, V: int, adj: List[List[int]]) -> bool:
        degree = [0] * V

        for i in range(V):
            degree[i] = len(adj[i])

        for i in range(V):
            if degree[i] % 2 != 0:
                return False

        return True


Approach1 = Solution


if __name__ == "__main__":
    s = Solution()
    # triangle: every degree is 2 -> circuit exists
    assert s.isEularCircuitExist(3, [[1, 2], [0, 2], [0, 1]]) is True
    # path 0-1-2: degrees 1,2,1 -> no circuit
    assert s.isEularCircuitExist(3, [[1], [0, 2], [1]]) is False
    print("ok")
