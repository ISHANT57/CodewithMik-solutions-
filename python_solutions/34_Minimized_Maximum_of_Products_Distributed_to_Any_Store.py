from typing import List

#     Not in instructor GitHub repo; code taken from the end of his video (screenshots).
#     Problem                     : Minimized Maximum of Products Distributed to Any Store (LeetCode 2064)
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store


# Approach (Using Binary Search on Answer - It asks to Minimize the Maximum which hints towards Binary Search On Answer)
# Intuition : Let x = max products any store gets. Each product type goes to stores entirely (one type per store),
#             so type q needs ceil(q/x) stores. x is feasible if sum(ceil(q/x)) <= m. Feasibility is monotonic in x
#             (bigger x -> fewer stores needed), so binary search x in [1, max(quantities)].
# T.C : O(n * log(MAX)), where n = length of quantities, MAX = max value in quantities
# S.C : O(1)
class Solution:

    def possibleToDistr(self, x: int, quantities: List[int], shops: int) -> bool:
        n = shops
        for products in quantities:
            n -= (products + x - 1) // x  # ceil(product/x)

            if n < 0:  # shops exhausted
                return False

        return True

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)

        l = 1
        r = max(quantities)

        result = 0

        while l <= r:
            mid = l + (r - l) // 2  # x

            if self.possibleToDistr(mid, quantities, n):
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result


if __name__ == "__main__":
    print(Solution().minimizedMaximum(6, [11, 6]))  # expected 3
    print(Solution().minimizedMaximum(7, [15, 10, 10]))  # expected 5
    print(Solution().minimizedMaximum(1, [100000]))  # expected 100000
