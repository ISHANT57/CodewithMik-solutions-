#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=N9YDsS9WJmM
#     Company Tags                : Google
#     Leetcode Link               : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List


# Approach (Binary Search with Duplicate Elimination)
# T.C : O(log n) on average, O(n) in worst case due to duplicate skipping
# S.C : O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        resultIdx = 0

        while l <= r:

            # remove duplicates from left
            while l < r and nums[l] == nums[l + 1]:
                l += 1

            # remove duplicates from right
            while l < r and nums[r] == nums[r - 1]:
                r -= 1

            mid = l + (r - l) // 2

            # update answer
            if nums[mid] < nums[resultIdx]:
                resultIdx = mid

            # minimum lies on right side
            if nums[mid] > nums[r]:
                l = mid + 1
            # minimum can be on left side
            else:
                r = mid - 1

        return nums[resultIdx]


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([1, 3, 5]))  # 1
    print(s.findMin([2, 2, 2, 0, 1]))  # 0
    print(s.findMin([3, 1, 3]))  # 1
