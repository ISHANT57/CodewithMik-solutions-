# Company Tags  : Google
# Leetcode Link : https://leetcode.com/problems/largest-component-size-by-common-factor/

import math
import sys
from typing import List

sys.setrecursionlimit(10**6)

# Approach-1 (Union Find - TLE)
class Solution:
    def commonFactor(self, a: int, b: int) -> bool:
        factor = 2

        while factor <= a and factor <= b:
            if a % factor == 0 and b % factor == 0:
                return True
            factor += 1
        return False

    def find(self, parent: List[int], i: int) -> int:
        if parent[i] == -1:
            return i

        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def Union(self, parent: List[int], x: int, y: int) -> None:
        parent[x] = y

    def largestComponentSize(self, nums: List[int]) -> int:
        edges = []  # list of (i, j) tuples
        n = len(nums)

        # This part is costly resulting in TLE (Building the graph)
        for i in range(n-1):
            for j in range(i+1, n):
                if self.commonFactor(nums[i], nums[j]):
                    edges.append((i, j))

        parent = [-1] * n
        result = 0

        for edge in edges:
            u = edge[0]
            v = edge[1]

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                self.Union(parent, x, y)

        mp = {}  # unordered_map<int, int>
        for i in range(n):
            set_ = self.find(parent, i)
            mp[set_] = mp.get(set_, 0) + 1
            result = max(result, mp[set_])
        return result

Approach1 = Solution


# Approach-2 (Union Find By Rank and Compression) (TLE)
class Solution:
    def commonFactor(self, a: int, b: int) -> bool:
        factor = 2

        while factor <= a and factor <= b:
            if a % factor == 0 and b % factor == 0:
                return True
            factor += 1
        return False

    def find(self, sub: List[List[int]], i: int) -> int:
        if sub[i][0] == i:
            return i

        sub[i][0] = self.find(sub, sub[i][0])
        return sub[i][0]

    def Union(self, sub: List[List[int]], x: int, y: int) -> None:
        x_s = self.find(sub, x)
        y_s = self.find(sub, y)

        if sub[x_s][1] > sub[y_s][1]:
            sub[y_s][0] = x_s
        elif sub[x_s][1] > sub[y_s][1]:
            sub[x_s][0] = y_s
        else:
            sub[y_s][0] = x_s
            sub[x_s][1] += 1

    def largestComponentSize(self, nums: List[int]) -> int:
        edges = []  # list of (i, j) tuples
        n = len(nums)

        # This part is costly resulting in TLE (Building the graph)
        for i in range(n-1):
            for j in range(i+1, n):
                if self.commonFactor(nums[i], nums[j]):
                    edges.append((i, j))

        sub = [[0, 0] for _ in range(n)]
        for i in range(n):
            sub[i][0] = i

        result = 0

        for edge in edges:
            u = edge[0]
            v = edge[1]

            x = self.find(sub, u)
            y = self.find(sub, v)

            if x != y:
                self.Union(sub, x, y)

        mp = {}  # unordered_map<int, int>
        for i in range(n):
            set_ = self.find(sub, i)
            mp[set_] = mp.get(set_, 0) + 1
            result = max(result, mp[set_])
        return result

Approach2 = Solution


# Approach-3 (Union Find With Precalculated Parent vector) ACCEPTED
# You can further optimise it using Union Find with Rank and Path Compresion
class Solution:

    def find(self, parent: List[int], i: int) -> int:
        if parent[i] == -1:
            return i

        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def Union(self, parent: List[int], x: int, y: int) -> None:
        x_s = self.find(parent, x)
        y_s = self.find(parent, y)

        if x_s != y_s:
            parent[x_s] = y_s

    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        parent = [-1] * 100001

        for x in nums:
            factor = 2
            while factor <= math.sqrt(x):
                if x % factor == 0:
                    self.Union(parent, factor, x)  # setting parent
                    self.Union(parent, x, x // factor)  # setting parent
                factor += 1

        mp = {}  # unordered_map<int, int>
        result = 0
        for x in nums:
            root = self.find(parent, x)
            mp[root] = mp.get(root, 0) + 1
            result = max(result, mp[root])
        return result

Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().largestComponentSize([4,6,15,35]) == 4
        assert S().largestComponentSize([20,50,9,63]) == 2
        assert S().largestComponentSize([2,3,6,7,4,12,21,39]) == 8
    print("ok")
