from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=kZGRjC7p3AE
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/most-beautiful-item-for-each-query


# Approach (simple binary search and preprocessing)
# T.C : O(nlogn + n + mlogn)
# S.C : O(1)
class Solution:

    def customBinarySearch(self, items: List[List[int]], queryPrice: int) -> int:
        l = 0
        r = len(items) - 1

        maxBeauty = 0

        while l <= r:
            mid = l + (r - l) // 2

            if items[mid][0] > queryPrice:
                r = mid - 1  # ignore current and right side items. Move to left now.
            else:
                maxBeauty = max(maxBeauty, items[mid][1])
                l = mid + 1

        return maxBeauty

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        m = len(queries)

        result = [0] * m

        # step-1 : Sort the array based on price in asencind order
        items.sort()  # {pricei, beautyi}

        maxBeautySeen = items[0][1]
        for i in range(1, n):
            maxBeautySeen = max(maxBeautySeen, items[i][1])
            items[i][1] = maxBeautySeen

        for i in range(m):
            queryPrice = queries[i]
            result[i] = self.customBinarySearch(items, queryPrice)

        return result


if __name__ == "__main__":
    print(Solution().maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))  # expected [2,4,5,5,6,6]
    print(Solution().maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], [1]))  # expected [4]
    print(Solution().maximumBeauty([[10, 1000]], [5]))  # expected [0]
