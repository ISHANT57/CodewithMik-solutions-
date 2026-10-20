from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=CSXkcvH8V-c
#     Company Tags                : AMAZON
#     Leetcode Link               : https://leetcode.com/problems/magnetic-force-between-two-balls


# Approach-1 (Using Binary Search on Answer)
# T.C : O(nlogn + n*log(max_force_diff))
# S.C : O(1)
class Solution:

    def possibleToPlace(self, force: int, position: List[int], m: int) -> bool:

        prev = position[0]
        countBalls = 1

        for i in range(1, len(position)):
            curr = position[i]

            if curr - prev >= force:
                countBalls += 1
                prev = curr

            if countBalls == m:
                break

        return countBalls == m

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        minForce = 1
        maxForce = position[n - 1] - position[0]  # better value (comment me batao)

        result = 0
        while minForce <= maxForce:
            midForce = minForce + (maxForce - minForce) // 2

            if self.possibleToPlace(midForce, position, m):
                result = midForce
                minForce = midForce + 1
            else:
                maxForce = midForce - 1

        return result


if __name__ == "__main__":
    print(Solution().maxDistance([1, 2, 3, 4, 7], 3))  # expected 3
    print(Solution().maxDistance([5, 4, 3, 2, 1, 1000000000], 2))  # expected 999999999
