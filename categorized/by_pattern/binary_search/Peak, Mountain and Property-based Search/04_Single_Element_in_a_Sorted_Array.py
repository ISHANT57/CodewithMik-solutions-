from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=cw5XhYeAU5o&list=PLpIkg8OmuX-LkgtrEF7eyyYWJM3m5tVQY&index=4
# (ASCII-art banner from the original C++ file omitted)
# Company Tags                : Amazon, D-E-Shaw, Ola Cabs, Codenation, Qualcomm, Microsoft
# Leetcode Link               : https://leetcode.com/problems/single-element-in-a-sorted-array/


# Approach : 1 (Using XOR operator) : O(n)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor_Value = 0

        for num in nums:
            xor_Value ^= num

        return xor_Value


Approach1 = Solution


# Approach : 2 (Using Binary Search) : O(log(n))
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            mid = l + (r - l) // 2
            isEven = (r - mid) % 2 == 0

            if nums[mid] == nums[mid + 1]:
                if isEven:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if isEven:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]

        return nums[l]  # or, nums[r]


Approach2 = Solution


# Approach : 3 (Another similar to Approach-2)
#     Some example to do a dry run to understand better:
#     {1, 1, 2, 2, 3, 4, 4}
#     {1, 1, 2, 3, 3}

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        h = n - 1

        while l < h:
            mid = l + (h - l) // 2

            isEven = (h - mid) % 2 == 0

            if nums[mid] == nums[mid + 1]:
                if isEven:
                    l = mid + 2
                else:
                    h = mid - 1
            else:
                if isEven:
                    h = mid
                else:
                    l = mid + 1

        return nums[h]


Approach3 = Solution


if __name__ == "__main__":
    for sol in (Approach1(), Approach2(), Approach3()):
        assert sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
        assert sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
        assert sol.singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]) == 3
        assert sol.singleNonDuplicate([1, 1, 2, 3, 3]) == 2
    print("OK")
