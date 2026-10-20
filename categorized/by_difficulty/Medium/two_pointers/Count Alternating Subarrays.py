from typing import List

# Scroll below to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=6BmOf92anPc
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/count-alternating-subarrays


# ******************************************************************** C++ *************************************************************
# T.C : O(n)
# S.C : O(1)
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        i = 0
        while i < n:  # C++ for-loop with i modified inside body, so while is used
            j = i

            while j + 1 < n and nums[j] != nums[j + 1]:
                j += 1

            length = j - i + 1  # 'len' in C++
            count += length * (length + 1) // 2
            i = j
            i += 1

        return count


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().countAlternatingSubarrays([0, 1, 1, 1]) == 5
    assert Solution().countAlternatingSubarrays([1, 0, 1, 0]) == 10
    print("ok")
