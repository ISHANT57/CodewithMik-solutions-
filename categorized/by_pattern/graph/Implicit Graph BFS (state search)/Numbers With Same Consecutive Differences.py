# Company Tags  : Flipkart
# Leetcode Link : https://leetcode.com/problems/numbers-with-same-consecutive-differences/

from typing import List
from collections import deque


# Approach-1 (DFS) (Time : O(9*2^(n-1))
class Solution:
    def __init__(self):
        self.result = []

    def generate(self, start, n, k, length):
        if length > n:
            return

        if length == n:
            self.result.append(start)
            return

        remain = start % 10
        if remain + k < 10:
            temp = start
            temp = (temp * 10) + remain + k
            self.generate(temp, n, k, length + 1)
        if remain - k >= 0 and k != 0:
            temp = start
            temp = (temp * 10) + remain - k
            self.generate(temp, n, k, length + 1)

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        for i in range(1, 10):
            self.generate(i, n, k, 1)
        return self.result


Approach1 = Solution


# Approach-2 (BFS) (Time : O(9*2^(n-1))
class Solution:
    def __init__(self):
        self.result = []

    def generate(self, n, k):
        que = deque()
        for i in range(1, 10):
            que.append(i)

        level = 1
        while level < n:  # Every level has (level) number of digits
            length = len(que)
            while length > 0:
                length -= 1
                curr = que.popleft()
                remain = curr % 10

                if remain - k >= 0:
                    que.append((curr * 10) + (remain - k))
                if remain + k <= 9 and k != 0:
                    que.append((curr * 10) + (remain + k))
            level += 1

        while que:
            self.result.append(que.popleft())

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.generate(n, k)
        return self.result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert sorted(S().numsSameConsecDiff(3, 7)) == [181, 292, 707, 818, 929]
        assert sorted(S().numsSameConsecDiff(2, 1)) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
    print("ok")
