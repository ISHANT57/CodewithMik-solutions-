#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=J_2DtfCHeSI
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/description/

from typing import List


# Approach (Binary Search on Answer)
# T.C : O(n * log(D)) where D = r-l+1
# S.C : O(1)
class Solution:
    def check(self, nums: List[int], x: int, y: int, d: int) -> bool:
        count = 0  # count of -1s
        prev = 0

        for i in range(len(nums)):
            if nums[i] == -1:
                # Trying all X in -1s or all Y in -1s
                if prev != 0 and min(abs(prev - x), abs(prev - y)) > d:
                    return False
                count += 1
            else:
                if count > 0:  # {-1, -1, -1, b}, {a, -1, -1, -1, b}
                    if prev != 0:
                        # Trying all X in -1s or all Y in -1s
                        absDiffResult = min(
                            max(abs(prev - x), abs(nums[i] - x)),
                            max(abs(prev - y), abs(nums[i] - y))
                        )
                    else:
                        # Trying all X in -1s or all Y in -1s
                        absDiffResult = min(abs(nums[i] - x), abs(nums[i] - y))

                    # Trying mixture of X and Y in -1s
                    canMixXAndY = (count >= 2 and abs(x - y) <= d)

                    if absDiffResult > d and not canMixXAndY:
                        return False

                prev = nums[i]
                count = 0

        return True

    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        min_val = 2**31 - 1  # INT_MAX
        max_val = 0
        maxAdsDiff = 0

        # l and r
        for i in range(n - 1):
            if nums[i] != -1 and nums[i + 1] != -1:  # {a, b}
                maxAdsDiff = max(maxAdsDiff, abs(nums[i] - nums[i + 1]))
            elif not (nums[i] == -1 and nums[i + 1] == -1):  # {-1, a}, {a, -1} , not of {-1, -1}
                val = max(nums[i], nums[i + 1])
                min_val = min(min_val, val)
                max_val = max(max_val, val)

        l = maxAdsDiff
        r = max_val - min_val

        result = maxAdsDiff
        while l <= r:
            d = l + (r - l) // 2
            x = min_val + d
            y = max_val - d
            if self.check(nums, x, y, d):
                result = d
                r = d - 1
            else:
                l = d + 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minDifference([1, 2, -1, 10, 8]))  # 4
    print(s.minDifference([-1, -1, -1]))  # 0
    print(s.minDifference([-1, 10, -1, 8]))  # 1
