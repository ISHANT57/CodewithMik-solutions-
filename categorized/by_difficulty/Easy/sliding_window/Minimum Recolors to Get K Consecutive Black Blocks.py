#     MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=3X6pwCDWFUM
#     Company Tags                  : Will update soon
#     Leetcode Link                 : https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks


# **************************************************************** C++ ****************************************************************
# Approach-1 (Brute Force)
# T.C : O(n*k)
# S.C : O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        result = k

        for i in range(n - k + 1):
            W = 0
            j = i
            while j - i + 1 <= k:
                if blocks[j] == 'W':
                    W += 1
                j += 1
            result = min(result, W)

        return result


Approach1 = Solution


# Approach-2 (Sliding Window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        i = 0
        j = 0

        ops = k
        W = 0

        while j < n:
            if blocks[j] == 'W':
                W += 1

            if j - i + 1 == k:
                ops = min(ops, W)

                if blocks[i] == 'W':
                    W -= 1
                i += 1
            j += 1

        return ops


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().minimumRecolors("WBBWWBBWBW", 7) == 3
        assert S().minimumRecolors("WBWBBBW", 2) == 0
    print("All tests passed")
