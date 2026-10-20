# Scroll below to see JAVA code also (Java sections skipped in this Python port)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=T3lhIT7hbl4
# Company Tag                 : will update later
# Leetcode Link               : https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating

INT_MAX = 2**31 - 1


# Approach-1 (Sliding Window + modifying input s = s+s)
# T.C : O(2*n) ~= O(n)
# S.C : O(2*n) for s1 and s2 and s+=s
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s += s

        s1, s2 = "", ""

        for i in range(2 * n):
            s1 += ('0' if i % 2 else '1')
            s2 += ('1' if i % 2 else '0')

        i, j = 0, 0
        result1, result2 = 0, 0
        result = INT_MAX

        while j < 2 * n:

            # expand window
            if s[j] != s1[j]: result1 += 1
            if s[j] != s2[j]: result2 += 1

            # shrink if window exceeds n
            if j - i + 1 > n:
                if s[i] != s1[i]: result1 -= 1
                if s[i] != s2[i]: result2 -= 1
                i += 1

            # window size exactly n
            if j - i + 1 == n:
                result = min(result, result1, result2)

            j += 1

        return result


Approach1 = Solution


# Approach-2 (Sliding Window + without modifying input)
# T.C : O(2*n) ~= O(n)
# S.C : O(2*n) for s1 and s2
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        s1, s2 = "", ""

        for i in range(2 * n):
            s1 += ('0' if i % 2 else '1')
            s2 += ('1' if i % 2 else '0')

        i, j = 0, 0
        result1, result2 = 0, 0
        result = INT_MAX

        while j < 2 * n:

            # expand window
            if s[j % n] != s1[j]:
                result1 += 1
            if s[j % n] != s2[j]:
                result2 += 1

            # shrink if window exceeds n
            if j - i + 1 > n:
                if s[i % n] != s1[i]:
                    result1 -= 1
                if s[i % n] != s2[i]:
                    result2 -= 1
                i += 1

            # window size exactly n
            if j - i + 1 == n:
                result = min(result, result1, result2)

            j += 1

        return result


Approach2 = Solution


# Approach-3 (Sliding Window + without modifying input)
# T.C : O(2*n) ~= O(n)
# S.C : O(1)
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        # khandani sliding window
        result = INT_MAX
        flip1 = 0
        flip2 = 0

        i = 0
        j = 0

        while j < 2 * n:

            expectedCharS1 = '1' if (j % 2) else '0'
            expectedCharS2 = '0' if (j % 2) else '1'

            if s[j % n] != expectedCharS1:
                flip1 += 1

            if s[j % n] != expectedCharS2:
                flip2 += 1

            if j - i + 1 > n:  # shrink the window from left
                expectedCharS1 = '1' if (i % 2) else '0'
                expectedCharS2 = '0' if (i % 2) else '1'

                if s[i % n] != expectedCharS1:
                    flip1 -= 1

                if s[i % n] != expectedCharS2:
                    flip2 -= 1

                i += 1

            if j - i + 1 == n:
                result = min(result, flip1, flip2)

            j += 1

        return result


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().minFlips("111000") == 2
        assert S().minFlips("010") == 0
        assert S().minFlips("1110") == 1
    print("all tests passed")
