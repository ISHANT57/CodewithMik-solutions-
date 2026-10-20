from typing import List

# MY YOUTUBE VIDEO FOR THIS Qn : https://www.youtube.com/watch?v=Jin6vO0MdzY&list=PLpIkg8OmuX-LkgtrEF7eyyYWJM3m5tVQY&index=2
# Company Tags                 : Amazon, Adobe, Microsoft, Morgan Stanley, Samsung, Snapdeal, Times Internet
# Leetcode Qn Link             : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findPivot(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:  # something wrong on right side. Possibly my answer lies in right side.
                l = mid + 1          # move right (Discarding mid, because it's greater than nums[r], so it can't be the minimum element)
            else:
                r = mid
        return nums[l]

    def findMin(self, nums: List[int]) -> int:
        return self.findPivot(nums)


# NOTE :
# What's wring with below logic :
# if(nums[mid] > nums[l])
#   l = mid+1;
# else
#   r = mid;
#
# Because, you are moving away from minimum element here.
# We should converge towards the side of array where the minimum element resides.


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    print("OK")
