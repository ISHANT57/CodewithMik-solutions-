from typing import List

# MY YOUTUBE VIDEO FOR THIS Qn : https://www.youtube.com/watch?v=hGLjwiPRh0U&list=PLpIkg8OmuX-K6A0sEPFxOSJh4_AjCGAFf&index=6
# Company Tags                 : Facebook, Amazon, Microsoft, Oracle
# Leetcode Link                : https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        closestSum = 100000

        for i in range(n - 2):

            l, r = i + 1, n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if abs(target - sum) < abs(target - closestSum):
                    closestSum = sum

                if sum > target:
                    r -= 1
                else:
                    l += 1
        return closestSum


Approach1 = Solution

if __name__ == "__main__":
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert Solution().threeSumClosest([0, 0, 0], 1) == 0
    print("ok")
