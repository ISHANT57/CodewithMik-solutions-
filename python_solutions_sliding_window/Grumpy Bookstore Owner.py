from typing import List

#    MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=kCxCE0_66vM
#    Company Tags                : will soon update
#    Leetcode Link               : https://leetcode.com/problems/grumpy-bookstore-owner


# ***************************************************************** C++ ******************************************************************************
# Approach - Sliding Window
# T.C : O(n)
# S.C : O(1)
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        unsat = 0

        # Calculate initial unsatisfied customers in the first 'minutes' window
        for i in range(minutes):
            unsat += customers[i] * grumpy[i]

        maxUnsat = unsat

        # Use two pointers i and j to define the sliding window of size 'minutes'
        i = 0
        j = minutes

        while j < n:
            unsat += customers[j] * grumpy[j]             # Include current element
            unsat -= customers[i] * grumpy[i]             # Remove element going out of window

            maxUnsat = max(maxUnsat, unsat)               # Update maxUnsat
            i += 1
            j += 1

        totalCustomers = maxUnsat

        # Calculate total satisfied customers
        for i in range(n):
            totalCustomers += customers[i] * (1 - grumpy[i])

        return totalCustomers


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16
    assert Solution().maxSatisfied([1], [0], 1) == 1
    print("All tests passed")
