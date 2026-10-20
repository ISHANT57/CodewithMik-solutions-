from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=hx8Ssz_3XSs
#     Company Tags                : will update soon
#     Leetcode Link               : https://leetcode.com/problems/find-k-th-smallest-pair-distance


# Approach-1 (storing the distances and finding the kth smallest)
# T.C : O(n^2)
# S.C : O(maxEl)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxEl = max(nums)
        vec = [0] * (maxEl + 1)

        # All pairs
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(nums[i] - nums[j])
                vec[d] += 1

        for d in range(maxEl + 1):
            k -= vec[d]
            if k <= 0:
                return d  # returning kth smallest distance
        return -1


# Approach-2 (nth element)
# T.C : O(n^2)
# S.C : O(n^2)
# Note: Python has no nth_element, so we use sorted(vec)[k-1] (O(n^2 log n) here, same result).
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        vec = [0] * (n * (n - 1) // 2)

        idx = 0
        for i in range(n):
            for j in range(i + 1, n):
                vec[idx] = abs(nums[i] - nums[j])
                idx += 1

        vec.sort()  # nth_element(begin(vec), begin(vec)+(k-1), end(vec)) -> Average : O(n) , Worst : O(n^2) in C++
        return vec[k - 1]


# Approach-3 (Binary Search + Sliding Window)
# T.C : O(nlogn + nlogM), where nlogn is for sorting nums and nlogM is becasue of binary search and sliding window
# S.C : O(1)
class Solution:

    # Find count of pairs having distance <= D
    def slidingWindowCount(self, nums: List[int], D: int) -> int:
        count = 0
        n = len(nums)
        i = 0
        j = 1

        while j < n:
            while nums[j] - nums[i] > D:
                i += 1
            count += j - i
            j += 1
        return count

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = nums[n - 1] - nums[0]
        result = 0

        while l <= r:
            mid = (l + r) // 2
            count = self.slidingWindowCount(nums, mid)

            if count < k:
                l = mid + 1
            else:
                result = mid  # Store the mid as a potential result
                r = mid - 1
        return result


if __name__ == "__main__":
    print(Solution().smallestDistancePair([1, 3, 1], 1))  # expected 0
    print(Solution().smallestDistancePair([1, 1, 1], 2))  # expected 0
    print(Solution().smallestDistancePair([1, 6, 1], 3))  # expected 5
