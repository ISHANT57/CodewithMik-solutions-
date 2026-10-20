#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=pjY5KaxYVIE
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays

from typing import List


# Approach (Binary Search on Answer)
# T.C : O(log(maxP-minP) * n * log(m)
# S.C : O(1)
class Solution:

    def findCountSmallest(self, nums1: List[int], nums2: List[int], midProduct: int) -> int:
        productsCount = 0

        n = len(nums2)

        for i in range(len(nums1)):
            # nums1[i]

            if nums1[i] >= 0:
                l = 0
                r = n - 1
                m = -1  # invalid index on left hand side

                while l <= r:
                    mid = l + (r - l) // 2
                    product = nums1[i] * nums2[mid]

                    if product <= midProduct:
                        m = mid
                        l = mid + 1
                    else:
                        r = mid - 1
                productsCount += (m + 1)  # covered by nums1[i]
            else:
                # product will be negative and right hand side will contain smaller products and left hand side larger
                l = 0
                r = n - 1
                m = n  # invalid index on the right hand side

                while l <= r:
                    mid = l + (r - l) // 2
                    product = nums1[i] * nums2[mid]

                    if product <= midProduct:
                        m = mid
                        r = mid - 1
                    else:
                        l = mid + 1

                productsCount += (n - m)
        return productsCount

    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0

        l = -10**10  # min product possible
        r = 10**10  # max product possible

        while l <= r:
            midProduct = l + (r - l) // 2

            # check if this is kth smallest or not

            countSmallest = self.findCountSmallest(nums1, nums2, midProduct)

            if countSmallest >= k:
                result = midProduct
                r = midProduct - 1
            else:
                l = midProduct + 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallestProduct([2, 5], [3, 4], 2))  # 8
    print(s.kthSmallestProduct([-4, -2, 0, 3], [2, 4], 6))  # 0
    print(s.kthSmallestProduct([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3))  # -6
