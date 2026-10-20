from typing import List

# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=HodpFY9Y6Vs
# Company Tags                : Amazon, ABCO, Flipkart
# Question Link               : https://practice.geeksforgeeks.org/problems/rotation4723/1


class Solution:
    def findKRotation(self, arr: List[int], n: int) -> int:
        l, r = 0, n - 1
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] < arr[r]:
                r = mid
            else:
                l = mid + 1
        return r


if __name__ == "__main__":
    s = Solution()
    assert s.findKRotation([5, 1, 2, 3, 4], 5) == 1
    assert s.findKRotation([1, 2, 3, 4, 5], 5) == 0
    assert s.findKRotation([4, 5, 6, 7, 0, 1, 2], 7) == 4
    print("OK")
