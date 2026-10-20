# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=WYBpATWlXWA
# Company Tags                : GOOGLE (onsite 2nd Round)
# Leetcode Link               : https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

from typing import List


# Using DSU
class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []

    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> None:
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        self.rank = [0] * n
        self.parent = list(range(n))

        for i in range(len(queries)):
            queries[i].append(i)

        lambda_ = lambda v: v[2]

        edgeList.sort(key=lambda_)
        queries.sort(key=lambda_)

        result = [False] * len(queries)

        j = 0
        for query in queries:

            u = query[0]
            v = query[1]
            w = query[2]
            idx = query[3]

            while j < len(edgeList) and edgeList[j][2] < w:
                self.Union(edgeList[j][0], edgeList[j][1])
                j += 1

            result[idx] = self.find(u) == self.find(v)

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().distanceLimitedPathsExist(3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]) == [False, True]
    assert Solution().distanceLimitedPathsExist(5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]) == [True, False]
    print("ok")
