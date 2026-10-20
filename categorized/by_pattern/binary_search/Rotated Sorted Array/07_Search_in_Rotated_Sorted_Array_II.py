from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=eneo_XPUEj0
# Company Tags                : Adobe, Amazon, Microsoft, Morgan Stanley, Samsung, Snapdeal, Times Internet
# Leetcode Link               : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/


class Solution:
    def pivot(self, nums: List[int], l: int, r: int) -> int:
        while l < r:

            while l < r and nums[l] == nums[l + 1]:
                l += 1

            while r < l and nums[r] == nums[r - 1]:
                r -= 1

            # You need to do what I did above because you'll fail in case like
            # [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
            # 2
            # Here, the nums[mid] <= nums[r] and
            # and we will cut down the right half but our pivot lies there
            # So, make it a RULE, whenever there are duplicate elements and you need to to something
            # like Binary Search, you need to ignore duplicates like done above
            # Similar Qn : "Smallest element in a rotated sorted array with duplicates"
            mid = l + (r - l) // 2

            if nums[mid] <= nums[r]:  # sorted part
                r = mid  # possibly my pivot
            else:
                l = mid + 1

        return r

    def binarySearch(self, nums: List[int], l: int, r: int, target: int) -> bool:
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        p = self.pivot(nums, 0, n - 1)
        # print("p = ", p)  (debug cout in the original, disabled here)
        if self.binarySearch(nums, 0, p - 1, target):
            return True

        return self.binarySearch(nums, p, n - 1, target)


if __name__ == "__main__":
    s = Solution()
    assert s.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert s.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    print("OK")
