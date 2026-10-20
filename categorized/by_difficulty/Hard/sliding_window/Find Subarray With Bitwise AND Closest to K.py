# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=BWBKtU8Euno
# Company Tags                : will soon update
# Leetcode Link               : https://leetcode.com/problems/find-subarray-with-bitwise-and-closest-to-k/description/

from typing import List


# Using sliding window and Bit knowledge
# T.C : O(n*32)
# S.C : O(1)
class Solution:

    def updateFreq(self, op: int, val: int, freqBits: List[int]) -> None:
        i = 0
        while val > 0:
            if val & 1:
                freqBits[i] += op  # +1 in case of adding and -1 in case of removing

            val //= 2
            i += 1

    def minimumDifference(self, nums: List[int], k: int) -> int:
        freqBits = [0] * 32

        n = len(nums)

        i = 0
        j = 0
        windowAnd = nums[0]
        result = 2**31 - 1  # INT_MAX

        while j < n:
            windowAnd = windowAnd & nums[j]
            self.updateFreq(1, nums[j], freqBits)

            result = min(result, abs(k - windowAnd))

            if windowAnd > k:
                j += 1
            elif windowAnd == k:  # can't get a better answer than 0 (we are dealing with absolute difference)
                return 0
            else:
                while i <= j and windowAnd < k:
                    self.updateFreq(-1, nums[i], freqBits)
                    i += 1
                    windowAnd = 0
                    for b in range(32):
                        if (j - i + 1) == freqBits[b]:  # jth bit of all numbers in the window (j-i+1) are set to 1
                            windowAnd = windowAnd | (1 << b)
                    result = min(result, abs(k - windowAnd))
                j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumDifference([1, 2, 4, 5], 3) == 1
    assert Solution().minimumDifference([1, 2, 1, 2], 2) == 0
    assert Solution().minimumDifference([1], 10) == 9
    print("ok")
