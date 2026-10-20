from typing import List
import bisect  # used only in Approach-2 (C++ lower_bound / upper_bound)

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=jpuDyt-ruFc&list=PLpIkg8OmuX-LkgtrEF7eyyYWJM3m5tVQY&index=1
# Company Tags                : LinkedIn, Amazon, Microsoft
# Leetcode Link               : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# GfG Practice                : https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x2041/1


# Approach-1 (Using Two Custom Binary Search)
# T.C : O(nlogn)
class Solution:
    def find_first_position(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        result = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                result = mid  # possibly my answer
                r = mid - 1   # but lets look at left more
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return result

    def find_last_position(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        result = -1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                result = mid  # possibly my answer
                l = mid + 1   # but lets look at right more
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.find_first_position(nums, target)
        r = self.find_last_position(nums, target)

        return [l, r]


Approach1 = Solution  # alias so the test below can reach this approach


# Approach-2 (Using C++ STL)  -> Python equivalent: bisect_left / bisect_right
# T.C : O(nlogn)
class Solution:

    # Approach-2
    def search_stl(self, nums: List[int], target: int) -> List[int]:
        # first element equal to or greater than target
        l = bisect.bisect_left(nums, target)

        # first element greater than target
        r = bisect.bisect_right(nums, target)

        # Why do we need this (nums[l] != target) ?
        # Because lower_bound returns first element which is equal or GREATER THAN target.
        # So, in case the target is not in the list, it will return first greater element than target which will be wrong
        if l == len(nums) or nums[l] != target:
            return [-1, -1]

        return [l, r - 1]

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        return self.search_stl(nums, target)  # Approach - 2


Approach2 = Solution


if __name__ == "__main__":
    for sol in (Approach1(), Approach2()):
        assert sol.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
        assert sol.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
        assert sol.searchRange([], 0) == [-1, -1]
    print("OK")
