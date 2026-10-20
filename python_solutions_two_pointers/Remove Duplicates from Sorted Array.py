# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=06ALbFrgIoQ
# Company Tags                : Facebook, Google, Amazon, Microsoft, Expedia, LinkedIn
# Leetcode Link               : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


# T.C : O(n)
# S.C : O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i, j = 0, 1

        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i + 1


Approach1 = Solution


if __name__ == "__main__":
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = Solution().removeDuplicates(a)
    assert k == 5 and a[:k] == [0, 1, 2, 3, 4]
    b = [1, 1, 2]
    k = Solution().removeDuplicates(b)
    assert k == 2 and b[:k] == [1, 2]
    print("ok")
