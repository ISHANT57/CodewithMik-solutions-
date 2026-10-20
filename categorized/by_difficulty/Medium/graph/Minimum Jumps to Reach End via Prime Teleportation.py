# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=lP3TWBQv1zs
# Company Tags                : will update later
# Leetcode Link               : https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation

from typing import List
from collections import deque, defaultdict


# ****************************************************************** C++ ******************************************************************
# Approach (Using BFS + Sieve)
# T.C : O(maxEL * loglog(maxEl))
# S.C : O(maxEl + n)
class Solution:
    def __init__(self):
        self.isPrime = []

    def buildSieve(self, maxEl: int) -> None:
        # fill isPrime
        self.isPrime = [True] * (maxEl + 1)

        self.isPrime[0] = False
        if maxEl >= 1:
            self.isPrime[1] = False

        num = 2
        while num * num <= maxEl:
            if self.isPrime[num]:

                for multiple in range(num * num, maxEl + 1, num):
                    self.isPrime[multiple] = False
            num += 1

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        mp = defaultdict(list)  # element -> indices
        maxEl = 0
        for i in range(n):
            mp[nums[i]].append(i)
            maxEl = max(maxEl, nums[i])

        # build isPrime vector using Sieve
        self.buildSieve(maxEl)  # O(maxEL * loglog(maxEl));

        que = deque()
        visited = [False] * n
        que.append(0)
        visited[0] = True

        seen = set()

        steps = 0
        # We visite each node only once - O(n)
        # O(n + maxEL * loglog(maxEl));
        while que:
            size = len(que)

            while size:
                size -= 1
                i = que.popleft()

                if i == n - 1:
                    return steps

                if i - 1 >= 0 and not visited[i - 1]:
                    que.append(i - 1)
                    visited[i - 1] = True

                if i + 1 <= n - 1 and not visited[i + 1]:
                    que.append(i + 1)
                    visited[i + 1] = True

                if not self.isPrime[nums[i]] or nums[i] in seen:
                    continue

                for multiple in range(nums[i], maxEl + 1, nums[i]):
                    if multiple not in mp:
                        continue

                    for j in mp[multiple]:
                        if not visited[j]:
                            que.append(j)
                            visited[j] = True

                seen.add(nums[i])

            steps += 1

        return steps


Approach1 = Solution

# (The Java section of the original file duplicates the above and is skipped.)


if __name__ == "__main__":
    assert Solution().minJumps([1, 2, 4, 6]) == 2
    assert Solution().minJumps([2, 3, 4, 7, 9]) == 2
    assert Solution().minJumps([4, 6, 5, 8]) == 3
    print("ok")
