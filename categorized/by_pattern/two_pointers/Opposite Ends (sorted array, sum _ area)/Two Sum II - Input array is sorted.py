# MY YOUTUBE VIDEO FOR THIS Qn : https://www.youtube.com/watch?v=gsSLay-wcaw
# Company Tags                 : Amazon
# Leetcode Link                : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
    print("ok")
