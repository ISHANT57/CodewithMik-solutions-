# Scroll below to see JAVA code also (Java section skipped in this Python port)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=3Bp3OVD1EGc
# Company Tags                : Google, Amazon, Microsoft, Codenation, FactSet, , Atlassian, MakeMyTrip, Streamoid Technologies, Media.net, Airbnb
# Leetcode Link               : https://leetcode.com/problems/minimum-window-substring/

from collections import defaultdict


# T.C : O(m+n) where m = length of s and n = length of t
# S.C : O(n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        mp = defaultdict(int)  # map<char, int>; missing keys read as 0 like C++ operator[]

        for ch in t:
            mp[ch] += 1

        requiredCount = len(t)
        i, j = 0, 0
        minStart = 0
        minWindow = 2**31 - 1  # INT_MAX
        while j < n:
            ch_j = s[j]
            if mp[ch_j] > 0:
                requiredCount -= 1

            mp[ch_j] -= 1

            while requiredCount == 0:  # try to shrink the window
                if minWindow > j - i + 1:
                    minWindow = j - i + 1
                    minStart = i

                ch_i = s[i]
                mp[ch_i] += 1
                if mp[ch_i] > 0:
                    requiredCount += 1
                i += 1

            j += 1  # Don't ever forget this :-)

        return "" if minWindow == 2**31 - 1 else s[minStart:minStart + minWindow]


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert Solution().minWindow("a", "a") == "a"
    assert Solution().minWindow("a", "aa") == ""
    print("all tests passed")
