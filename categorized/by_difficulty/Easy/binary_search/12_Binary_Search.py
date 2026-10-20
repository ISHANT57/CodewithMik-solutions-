from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Rxf93Ey1fpA
# Company Tags                : Everyone :-)
# Leetcode Link               : https://leetcode.com/problems/binary-search/

# Iterative : O(log(n))
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1

        mid = 0

        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


Iterative = Solution


# Recursive : O(log(n))
class Solution:

    def solve(self, nums: List[int], l: int, r: int, target: int) -> int:
        if l > r:
            return -1

        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.solve(nums, mid + 1, r, target)
        else:
            return self.solve(nums, l, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        return self.solve(nums, 0, n - 1, target)


Recursive = Solution


if __name__ == "__main__":
    for sol in (Iterative(), Recursive()):
        assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
        assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("OK")
