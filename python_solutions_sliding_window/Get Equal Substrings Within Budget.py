#    MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=MF2MgJQuFhA
#    Company Tags                : Will soon update
#    Leetcode Link               : https://leetcode.com/problems/get-equal-substrings-within-budget


# ****************************************************** C++ ******************************************************
# T.C : O(n)
# S.C : O(1)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        maxLen = 0
        currCost = 0

        i = 0
        j = 0
        while j < n:
            currCost += abs(ord(s[j]) - ord(t[j]))

            while currCost > maxCost:
                currCost -= abs(ord(s[i]) - ord(t[i]))
                i += 1

            maxLen = max(maxLen, j - i + 1)
            j += 1

        return maxLen


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().equalSubstring("abcd", "bcdf", 3) == 3
    assert Solution().equalSubstring("abcd", "cdef", 3) == 1
    assert Solution().equalSubstring("abcd", "acde", 0) == 1
    print("All tests passed")
