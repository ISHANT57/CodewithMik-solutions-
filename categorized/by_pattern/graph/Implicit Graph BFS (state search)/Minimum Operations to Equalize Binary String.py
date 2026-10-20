# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=cH6VFgRaRW0
# Company Tags                : Will update soon
# Leetcode Link               : https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/

from bisect import bisect_left
from collections import deque

# ************************************************************ C++ ************************************************
# Approach-1 - Brute Force
# T.C : O(n*k) ~ O(n^2)
# S.C : O(n)
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)

        startZeros = 0
        for ch in s:
            if ch == '0':
                startZeros += 1

        if startZeros == 0:
            return 0  # no operations required

        operations = [-1] * (n+1)
        # operations[z] = min operations required to reach state in which we have z 0s

        que = deque()
        que.append(startZeros)
        operations[startZeros] = 0

        while que:
            z = que.popleft()

            minF = max(0, k-n+z)
            maxF = min(k, z)

            for f in range(minF, maxF+1):
                newZ = z + k - 2*f

                if operations[newZ] == -1:
                    operations[newZ] = operations[z] + 1

                    if newZ == 0:
                        return operations[newZ]

                    que.append(newZ)

        return -1

Approach1 = Solution


# Approach-2 - Optimal - Skipping already visited states
# T.C : O(n*logn)
# S.C : O(n)
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)

        startZeros = 0
        for ch in s:
            if ch == '0':
                startZeros += 1

        if startZeros == 0:
            return 0  # no operations required

        operations = [-1] * (n+1)
        # operations[z] = min operations required to reach state in which we have z 0s

        # set<int> -> sorted list + bisect (erase = del by index; erasing from a list is O(n) here)
        evenSet = []
        oddSet = []

        for count in range(n+1):
            if count % 2 == 0:
                evenSet.append(count)
            else:
                oddSet.append(count)

        que = deque()
        que.append(startZeros)
        operations[startZeros] = 0
        if startZeros % 2 == 0:
            del evenSet[bisect_left(evenSet, startZeros)]
        else:
            del oddSet[bisect_left(oddSet, startZeros)]

        while que:
            z = que.popleft()

            min_new_z = z + k - 2*min(k, z)
            max_new_z = z + k - 2*max(0, k-n+z)

            currSet = evenSet if min_new_z % 2 == 0 else oddSet

            it = bisect_left(currSet, min_new_z)  # lower_bound

            while it < len(currSet) and currSet[it] <= max_new_z:
                newZ = currSet[it]

                if operations[newZ] == -1:
                    operations[newZ] = operations[z] + 1

                    if newZ == 0:
                        return operations[newZ]

                    que.append(newZ)

                del currSet[it]  # it = currSet.erase(it) -> index now points to next element

        return -1

Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().minOperations("110", 1) == 1
        assert S().minOperations("0101", 3) == 2
        assert S().minOperations("101", 2) == -1
    print("ok")
