from typing import List

# Scroll down to see JAVA code also (Java section skipped in this Python port)
#
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=_cBWWebTVpI&list=PLpIkg8OmuX-K6A0sEPFxOSJh4_AjCGAFf&index=4
# Company Tags                : Amazon, Facebook, Google
# Question on GfG             : Find triplets with zero sum (https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1)
# Leetcode Qn Link            : https://leetcode.com/problems/3sum/


# ************************************************ C++ ************************************************
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def twoSum(self, nums: List[int], k: int, result: List[List[int]], target: int) -> None:
        # Two pointer technique (Sorted array) Things you must not forget in interviews

        i, j = k, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                result.append([-target, nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1  # Things you must not forget in interviews
                j -= 1  # Things you must not forget in interviews

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:  # Things you must not forget in interviews
            return []
        result: List[List[int]] = []
        nums.sort()
        for i in range(len(nums) - 2):  # (i<nums.size()-2)Things you must not forget in interviews
            if i != 0 and nums[i] == nums[i - 1]:  # Things you must not forget in interviews
                continue
            self.twoSum(nums, i + 1, result, -nums[i])
        return result


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([0, 1, 1]) == []
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
    print("ok")
