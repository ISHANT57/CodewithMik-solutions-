# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=TI-xIXH4EnE
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/greatest-common-divisor-traversal/

from typing import List


########################################## Python (converted from C++) ##########################################
# T.C : O(N * sqrt(N) * alpha) where alpha is for Union Find operations. But it's small , so we can ignore it to O(1) as average --> O(N*sqrt(N))
# S.C : O(N)
class DSU:
    def __init__(self, n: int):
        self.parent = [0] * n
        self.size = [0] * n
        self.numberOfComponents = n

        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

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

        if self.size[x_parent] > self.size[y_parent]:
            self.parent[y_parent] = x_parent
            self.size[x_parent] += self.size[y_parent]
        elif self.size[x_parent] < self.size[y_parent]:
            self.parent[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]
        else:
            self.parent[x_parent] = y_parent
            self.size[y_parent] += self.size[x_parent]

        self.numberOfComponents -= 1

    def maxSize(self) -> int:
        return self.numberOfComponents


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = DSU(n)

        m = max(nums)

        first = [-1] * (m + 1)

        for i in range(n):

            prime = 2
            while prime * prime <= nums[i]:
                if nums[i] % prime != 0:
                    prime += 1
                    continue

                if first[prime] != -1:
                    dsu.Union(first[prime], i)
                else:
                    first[prime] = i

                while nums[i] % prime == 0:
                    nums[i] //= prime
                prime += 1

            if nums[i] > 1:
                if first[nums[i]] != -1:
                    dsu.Union(first[nums[i]], i)
                else:
                    first[nums[i]] = i

        return dsu.maxSize() == 1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().canTraverseAllPairs([2, 3, 6]) is True
    assert Solution().canTraverseAllPairs([3, 9, 5]) is False
    assert Solution().canTraverseAllPairs([4, 3, 12, 8]) is True
    print("ok")
