from typing import List

# Company Tags  : Bloomberg, Facebook, Google, Amazon, Adobe
# Leetcode Link : https://leetcode.com/problems/container-with-most-water/

# Why does my solution given below works ?
#
# Idea / Proof (Gathered from Discussion Section of Leetcode from some intelligent programmers) :
#     The widest container (using first and last line) is a good candidate, because of its width.
#     Its water level is the height of the smaller one of first and last line. All other containers
#     are less wide and thus would need a higher water level in order to hold more water. The smaller
#     one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.


# Approach-1 (Two pointer Greedy (O(N))
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1

        water = 0
        while i < j:

            # start from the smallest one and calculate water
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            water = max(water, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return water


Approach1 = Solution


# Approach-2 (Two pointer Greedy (O(N)) (It's similar to Approach-1)
# Just that we are eliminating heights at one go
# NOTE: the C++ source had a stray, unfinished line "if(height[i] <" before the while loops
# (does not compile); it is omitted here, the rest of the algorithm is unchanged.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1

        water = 0
        while i < j:

            # start from the smallest one and calculate water
            h = min(height[i], height[j])
            w = j - i
            area = h * w
            water = max(water, area)

            # Then move towards large one because we can have better answer
            while i < j and height[i] <= h:
                i += 1
            # Same,  move towards large one because we can have better answer
            while i < j and height[j] <= h:
                j -= 1

        return water


Approach2 = Solution

if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
        assert S().maxArea([1, 1]) == 1
    print("ok")
