# Scroll below to see JAVA code also (Java section skipped in this Python port)
# MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=X1LgOR-_pJE
# Company Tags                  : Will update soon
# Leetcode Link                 : https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

from typing import List


# Approach (Using classic sliding window template + using set/map to keep distinct element)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        result = 0
        currWindowSum = 0
        st = set()  # unordered_set<int>

        while j < len(nums):
            # Adjust the window if nums[j] is already in the set
            while nums[j] in st:
                currWindowSum -= nums[i]
                st.discard(nums[i])
                i += 1

            currWindowSum += nums[j]
            st.add(nums[j])

            # Check if the window size is equal to k
            if j - i + 1 == k:
                result = max(result, currWindowSum)

                # Shrink the window from the left
                currWindowSum -= nums[i]
                st.discard(nums[i])
                i += 1

            j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3) == 15
    assert Solution().maximumSubarraySum([4, 4, 4], 3) == 0
    print("all tests passed")
