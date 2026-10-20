from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=t2p4Sn0Qepo
#     Company Tags                : will update soon
#     Leetcode Link               : https://leetcode.com/problems/longest-nice-subarray/description/


# ********************************************************************** C++ **********************************************************************
# Approach-1 (Brute Force)
# T.C : O(n^3)
# S.C : O(1)
class Solution:
    def isNice(self, nums: List[int], start: int, end: int) -> bool:
        mask = 0
        for i in range(start, end + 1):
            if (mask & nums[i]) != 0:
                return False
            mask |= nums[i]
        return True

    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            for j in range(i, n):
                if self.isNice(nums, i, j):
                    result = max(result, j - i + 1)
                else:
                    break  # No need to check further, as adding more elements will keep failing

        return result


Approach1 = Solution


# Approach-2 (Better)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        result = 0

        for i in range(n):
            mask = 0

            for j in range(i, n):
                if (mask & nums[j]) != 0:
                    break

                result = max(result, j - i + 1)
                mask = (mask | nums[j])

        return result


Approach2 = Solution


# Approach-3 (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(1)
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        j = 0

        result = 1
        mask = 0

        while j < n:

            while (mask & nums[j]) != 0:  # keep shrinking
                mask = (mask ^ nums[i])
                i += 1

            result = max(result, j - i + 1)
            mask = (mask | nums[j])
            j += 1

        return result


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().longestNiceSubarray([1, 3, 8, 48, 10]) == 3
        assert S().longestNiceSubarray([3, 1, 5, 11, 13]) == 1
    print("All tests passed")
