# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=lWU1wI7koGk
# Company Tags                : Meta
# Leetcode Link               : https://leetcode.com/problems/minimize-maximum-of-array/
# Similar Leetcode Qn         : https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

from typing import List


class Solution:

    def isValid(self, nums: List[int], mid_max: int, n: int) -> bool:

        arr = list(nums)  # Python ints are arbitrary precision (C++ used long long)

        for i in range(n - 1):

            if arr[i] > mid_max:
                return False

            buffer = mid_max - arr[i]

            arr[i + 1] = arr[i + 1] - buffer

        return arr[n - 1] <= mid_max

    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)

        maxL = 0
        maxR = max(nums)

        result = 0

        while maxL <= maxR:

            mid_max = maxL + (maxR - maxL) // 2

            if self.isValid(nums, mid_max, n):
                result = mid_max
                maxR = mid_max - 1
            else:
                maxL = mid_max + 1

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.minimizeArrayValue([3, 7, 1, 6]) == 5
    assert s.minimizeArrayValue([10, 1]) == 10
    print("ok")
