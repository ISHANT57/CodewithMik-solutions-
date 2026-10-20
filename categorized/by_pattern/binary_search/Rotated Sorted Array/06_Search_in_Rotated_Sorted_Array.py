from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=U1VsdRgVevY
# Company Tags                : Google, Adobe, Amazon, Microsoft, Morgan Stanley, Samsung, Snapdeal, Times Internet
# Leetcode Link               : https://leetcode.com/problems/search-in-rotated-sorted-array/
# Similar GfG Link            : https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1


class Solution:
    def find_pivot(self, nums: List[int], l: int, r: int) -> int:
        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return r

    def binary_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.find_pivot(nums, 0, n - 1)

        if nums[pivot] == target:
            return pivot

        idx = -1
        idx = self.binary_search(nums, pivot + 1, n - 1, target)
        if idx != -1:
            return idx
        idx = self.binary_search(nums, 0, pivot - 1, target)
        return idx


if __name__ == "__main__":
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    assert s.search([1], 1) == 0
    print("OK")
