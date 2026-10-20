# My YouTube Video Link : https://www.youtube.com/watch?v=Iaz-8ZQYUvs
# Company Tags          : will update soon
# Leetcode Link         : https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/

from typing import List

# (Java section of the original is not ported: this file is the Python 3 port of the C++ code)

# ************************************ C++ (ported to Python) ****************************************
# T.C : O(n * log(n))
# S.C : O(n)
class Solution:
    def IsPossible(self, len: int, nums: List[int], prefix: List[int], K: int, n: int) -> bool:
        if len == 0:
            return False

        i = 0
        j = len - 1

        while j < n:
            target_idx = (i + j) // 2
            target = nums[target_idx]

            operations_left = 0
            operations_right = 0

            if target_idx == 0:
                operations_left = 0
            else:
                operations_left = abs(((target_idx - i) * target) - (prefix[target_idx - 1] - (prefix[i - 1] if i > 0 else 0)))

            operations_right = abs(((j - target_idx) * target) - (prefix[j] - prefix[target_idx]))

            if operations_right + operations_left <= K:
                return True

            i += 1
            j += 1

        return False

    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        min_score = 1
        max_score = n
        result_score = 1

        while min_score <= max_score:
            mid = (min_score + max_score) // 2

            if self.IsPossible(mid, nums, prefix, k, n):
                result_score = mid
                min_score = mid + 1
            else:
                max_score = mid - 1

        return result_score


if __name__ == "__main__":
    s = Solution()
    assert s.maxFrequencyScore([1, 2, 6, 4], 3) == 3
    assert s.maxFrequencyScore([1, 4, 4, 2, 4], 0) == 3
    print("ok")
