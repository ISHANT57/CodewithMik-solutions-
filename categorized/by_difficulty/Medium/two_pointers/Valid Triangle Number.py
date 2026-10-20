# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=lblGlKlXUBM
# Company Tags                  : will update later
# Leetcode Link                 : https://leetcode.com/problems/valid-triangle-number

from typing import List


# Approach-1 (Brute Force)
# T.C : O(n^3)
# S.C : O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        # check all triplets
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (nums[i] + nums[j] > nums[k] and
                            nums[i] + nums[k] > nums[j] and
                            nums[j] + nums[k] > nums[i]):
                        count += 1

        return count


Approach1 = Solution


# Approach-2 (Binary Search)
# T.C : O(n^2 * logn)
# S.C : O(1)
class Solution:
    def binarySearch(self, nums: List[int], l: int, r: int, target: int) -> int:
        k = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                k = mid         # mid is valid
                l = mid + 1     # try to go right
            else:
                r = mid - 1     # go left
        return k

    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0

        for i in range(n):
            if nums[i] == 0:
                continue

            for j in range(i + 1, n):

                sum = nums[i] + nums[j]  # sum of two sides
                k = self.binarySearch(nums, j + 1, n - 1, sum)
                if k != -1:
                    count += (k - j)

        return count


Approach2 = Solution


# Approach-3 (Two Pointer)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0

        for k in range(n - 1, 1, -1):    # k is the largest side
            i, j = 0, k - 1              # two pointers

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)     # all pairs (i..j-1, j) will satisfy the inequality
                    j -= 1
                else:
                    i += 1

        return count


Approach3 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2, Approach3):
        assert A().triangleNumber([2, 2, 3, 4]) == 3
        assert A().triangleNumber([4, 2, 3, 4]) == 4
        assert A().triangleNumber([0, 0, 0]) == 0
    print("ok")
