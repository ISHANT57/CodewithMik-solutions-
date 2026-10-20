# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=skEofEGj46Y
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/


# Using simple 2 Pointers
# T.C : O(n)
# S.C : O(1)
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        i, j = 0, n - 1

        while i < j and s[i] == s[j]:
            ch = s[i]

            while i < j and s[i] == ch:
                i += 1

            while j >= i and s[j] == ch:
                j -= 1

        return j - i + 1


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minimumLength("ca") == 2
    assert Solution().minimumLength("cabaabac") == 0
    assert Solution().minimumLength("aabccabba") == 3
    print("ok")
