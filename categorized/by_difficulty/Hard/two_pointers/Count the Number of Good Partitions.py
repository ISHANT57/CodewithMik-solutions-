from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=fyyjpElDeuY
# Company Tags                : I will update soon
# Leetcode Link               : https://leetcode.com/problems/count-the-number-of-good-partitions/

# ************************************************************ C++ ************************************************************
# Approach (Using simple 2 Pointer)
# T.C : O(n)
# S.C : O(n)
class Solution:
    M = 10**9 + 7

    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        M = self.M
        n = len(nums)
        last_index = {}  # number, last index  (unordered_map -> dict)

        for i in range(n):
            last_index[nums[i]] = i

        i = 0
        j = max(0, last_index[nums[0]])

        result = 1
        while i < n:
            if i > j:  # we found one partition
                result = (result * 2) % M

            j = max(j, last_index[nums[i]])
            i += 1

        return result


Approach1 = Solution

# (The second section in the source is the Java version of the same approach; skipped.)

if __name__ == "__main__":
    assert Solution().numberOfGoodPartitions([1, 2, 3, 4]) == 8
    assert Solution().numberOfGoodPartitions([1, 1, 1, 1]) == 1
    assert Solution().numberOfGoodPartitions([1, 2, 1, 3]) == 2
    print("ok")
