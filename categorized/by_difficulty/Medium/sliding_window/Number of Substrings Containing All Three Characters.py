# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=wafDgldM9MA
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

# Approach (Sliding Window Khandani Template)
# T.C : O(2*n) ~ O(n)
# S.C : O(1)
from typing import List


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        result = 0

        mp = [0] * 3  # 0 - a, 1 - b, 2 - c

        i = 0
        j = 0
        while j < n:
            ch = s[j]
            mp[ord(ch) - ord('a')] += 1

            while mp[0] > 0 and mp[1] > 0 and mp[2] > 0:
                result += (n - j)

                mp[ord(s[i]) - ord('a')] -= 1
                i += 1

            j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().numberOfSubstrings("abcabc") == 10
    assert Solution().numberOfSubstrings("aaacb") == 3
    assert Solution().numberOfSubstrings("abc") == 1
    print("All tests passed")
