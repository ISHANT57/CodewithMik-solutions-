# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=oWp--NIqWac&t=16s
# Company Tags                : Microsoft, Google(with variation)
# Leetcode Link               : https://leetcode.com/problems/guess-number-higher-or-lower/

# Mock of LeetCode's predefined API, for local testing only (on LeetCode, guess() is provided).
pick = 6


def guess(num: int) -> int:
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = l + (r - l) // 2
            val = guess(mid)

            if val == -1:
                r = mid - 1
            elif val == 1:
                l = mid + 1
            else:
                return mid

        return -1


if __name__ == "__main__":
    s = Solution()
    pick = 6
    assert s.guessNumber(10) == 6
    pick = 1
    assert s.guessNumber(1) == 1
    pick = 1
    assert s.guessNumber(2) == 1
    print("OK")
