from typing import List

# Scroll below to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=TGaKkfMe_00
# Company Tags                  : Will update later
# Leetcode Link                 : https://leetcode.com/problems/two-furthest-houses-with-different-colors


# *************************************************************** C++ *************************************************
# Approach-1 (Brute Force)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    result = max(result, j - i)
        return result


Approach1 = Solution


# Approach-2 (Improved Brute Force)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        result = 0
        for i in range(n):
            for j in range(n - 1, i, -1):
                if colors[i] != colors[j]:
                    result = max(result, j - i)
                    break
        return result


Approach2 = Solution


# Approach-3 (2 Pass Solution)
# T.C : O(2*n) ~= O(n)
# S.C : O(1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        result = 0

        i = 0
        while colors[i] == colors[n - 1]:
            i += 1

        result = max(result, abs(i - (n - 1)))

        i = n - 1
        while colors[0] == colors[i]:
            i -= 1

        result = max(result, i)

        return result


Approach3 = Solution


# Approach-4 (1 Pass Solution)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        result = 0

        for i in range(n):
            if colors[i] != colors[0]:
                result = max(result, i)

            if colors[i] != colors[n - 1]:
                result = max(result, abs(i - (n - 1)))

        return result


Approach4 = Solution

if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3, Approach4):
        assert S().maxDistance([1, 1, 1, 6, 1, 1, 1]) == 3
        assert S().maxDistance([1, 8, 3, 8, 3]) == 4
        assert S().maxDistance([0, 1]) == 1
    print("ok")
