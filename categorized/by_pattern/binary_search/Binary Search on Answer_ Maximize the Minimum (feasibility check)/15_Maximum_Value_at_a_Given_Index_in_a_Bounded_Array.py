# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=d50vvNSrqfk
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

# Using Binary Search
class Solution:

    def getSumElements(self, count: int, val: int) -> int:

        return val * count - (count * (count + 1)) // 2

    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        left = 1
        right = maxSum

        mid_val = 0
        result = 0

        while left <= right:

            mid_val = left + (right - left) // 2

            left_count = min(index, mid_val - 1)

            left_sum = self.getSumElements(left_count, mid_val)

            left_sum += max(0, index - mid_val + 1)

            right_count = min(n - index - 1, mid_val - 1)

            right_sum = self.getSumElements(right_count, mid_val)

            right_sum += max(0, n - index - 1 - mid_val + 1)

            if left_sum + right_sum + mid_val <= maxSum:
                result = max(result, mid_val)

                left = mid_val + 1
            else:
                right = mid_val - 1

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.maxValue(4, 2, 6) == 2
    assert s.maxValue(6, 1, 10) == 3
    print("ok")
