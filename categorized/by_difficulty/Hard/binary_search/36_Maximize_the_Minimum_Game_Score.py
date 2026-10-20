from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=mKDi2RYriLE
#     Company Tags                : Will update soon
#     Leetcode Link               : https://leetcode.com/problems/maximize-the-minimum-game-score


# Approach - Using Binary Search on Answer
# T.C : O(n * log(max point))
# S.C : O(1)
class Solution:
    # typedef long long ll  (Python ints are arbitrary precision)

    def isPossible(self, target: int, m: int, points: List[int], n: int) -> bool:
        moves = 0

        advanceGamesToNext = 0
        normalMove = 0

        i = 0
        while i < n and moves <= m:
            gamePoint = points[i]

            games = (target + gamePoint - 1) // gamePoint  # ceil(target/gamePoint);
            # cile(a/b) = (a + b - 1) / b

            if advanceGamesToNext >= games:
                advanceGamesToNext = 0
                normalMove += 1
            else:
                pointsAlreadyCovered = advanceGamesToNext * gamePoint

                games = (target - pointsAlreadyCovered + gamePoint - 1) // gamePoint
                # ceil((target - pointsAlreadyCovered) / gamePoint);

                moves += (2 * games) - 1

                advanceGamesToNext = max(games - 1, 0)

                moves += normalMove

                normalMove = 0
            i += 1

        return moves <= m

    def maxScore(self, points: List[int], m: int) -> int:
        n = len(points)

        l = 1
        r = 10**15  # 10^15
        # 10^9 * 10^6 = 10^15

        result = 0

        while l <= r:
            mid = l + (r - l) // 2  # target score

            if self.isPossible(mid, m, points, n) == True:
                result = mid
                l = mid + 1
            else:
                r = mid - 1

        return result


if __name__ == "__main__":
    print(Solution().maxScore([2, 4], 3))  # expected 4
    print(Solution().maxScore([1, 2, 3], 5))  # expected 2
