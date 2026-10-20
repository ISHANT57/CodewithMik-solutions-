# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=B3Wgf-g6i-k
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

from typing import List


############################################ Python (converted from C++) ############################################
# T.C :
#     The time complexity of the union-find operations (with path compression) is approximately O(α(n)),
#     where α is the inverse Ackermann function, which is practically constant for all reasonable values of n.
#     The time complexity of processing each edge and each query is O(1).
#     Therefore, the overall time complexity of the algorithm is O(E + Qα(n)), where E is the number of edges,
#     Q is the number of queries, and α(n) is the inverse Ackermann function.
# S.C : O(n)
class Solution:

    def __init__(self):
        self.parent = []

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        self.parent[y] = x

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        self.parent = [0] * n
        cost = [0] * n  # Store "And operation" cost of each component

        for i in range(n):
            self.parent[i] = i
            cost[i] = -1

        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]

            parent_u = self.find(u)
            parent_v = self.find(v)

            if parent_u != parent_v:
                cost[parent_u] &= cost[parent_v]
                self.Union(parent_u, parent_v)

            cost[parent_u] &= w

        res = []
        for q in query:
            s = q[0]
            t = q[1]

            p1 = self.find(s)
            p2 = self.find(t)

            if s == t:
                res.append(0)
            elif p1 != p2:
                res.append(-1)
            else:
                res.append(cost[p1])
        return res


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumCost(5, [[0, 1, 7], [1, 3, 7], [1, 2, 1]], [[0, 3], [3, 4]]) == [1, -1]
    assert Solution().minimumCost(3, [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], [[1, 2]]) == [0]
    print("ok")
