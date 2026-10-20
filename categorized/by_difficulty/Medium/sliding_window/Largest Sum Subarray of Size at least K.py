from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn :
#     Company Tags                : Facebook, Paytm, Myntra
#     GfG Link                    : https://www.geeksforgeeks.org/problems/largest-sum-subarray-of-size-at-least-k3121/1


# ****************************************************************** C++ ******************************************************************
# Approach (Using Sliding Window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def maxSumWithK(self, arr: List[int], n: int, k: int) -> int:
        sum = 0
        result = -2**31  # INT_MIN
        i = 0
        trail = 0

        for j in range(n):
            sum += arr[j]

            if j - i + 1 == k:
                result = max(result, sum)
            elif j - i + 1 > k:
                trail += arr[i]

                if trail < 0:
                    sum -= trail
                    trail = 0

                result = max(result, sum)
                i += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxSumWithK([1, 2, 3, 4], 4, 2) == 10
    assert Solution().maxSumWithK([-4, -2, 1, -3], 4, 2) == -1
    assert Solution().maxSumWithK([1, 1, 1, 1, 1, 1], 6, 2) == 6
    print("All tests passed")
