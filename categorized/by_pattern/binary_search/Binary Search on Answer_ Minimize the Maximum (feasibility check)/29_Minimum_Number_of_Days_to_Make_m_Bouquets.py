from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=erWfh_hBF80
#     Company Tags                : AMAZON
#     Leetcode Link               : https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets


# Approach - Using "Binary Search on Answer"
# T.C : O(n * log(max_d)), n is the number of flowers and max_d is the highest value in the array bloomDay.
# S.C : O(1)
class Solution:
    def getNumOfBouquets(self, bloomDay: List[int], mid: int, k: int) -> int:
        numOfBouquets = 0
        consecutive_count = 0

        # Find count of consecutive flowers you can pick at mid day.
        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                consecutive_count += 1
            else:
                consecutive_count = 0
            if consecutive_count == k:
                numOfBouquets += 1
                consecutive_count = 0
        return numOfBouquets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start_day = 0
        end_day = max(bloomDay)

        minDays = -1

        while start_day <= end_day:
            mid = start_day + (end_day - start_day) // 2

            if self.getNumOfBouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end_day = mid - 1
            else:
                start_day = mid + 1

        return minDays


if __name__ == "__main__":
    print(Solution().minDays([1, 10, 3, 10, 2], 3, 1))   # expected 3
    print(Solution().minDays([1, 10, 3, 10, 2], 3, 2))   # expected -1
    print(Solution().minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))  # expected 12
