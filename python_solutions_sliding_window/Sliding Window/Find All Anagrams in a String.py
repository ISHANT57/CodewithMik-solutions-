# Company Tags  : Microsoft, Google, Amazon
# Leetcode Link : https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List


# Similar to normal sliding window qns
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr = [0] * 26

        m = len(s)
        n = len(p)

        for ch in p:
            arr[ord(ch) - ord('a')] += 1

        i = 0
        j = 0
        result = []

        while j < m:
            arr[ord(s[j]) - ord('a')] -= 1

            if j - i + 1 == n:
                if arr == [0] * 26:
                    result.append(i)

                arr[ord(s[i]) - ord('a')] += 1
                i += 1
            j += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]
    print("ok")
