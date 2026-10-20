# MY YOUTUBE VIDEO ON THIS QN : https://www.youtube.com/watch?v=mrUBUWb23hk
# Company Tags    		: Amazon, Intuit, Microsoft, Flipkart
# Qn Link      		: https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1#

from typing import List

# T.C : O(n)
# S.C : O(1)
class Solution:
    def allZero(self, count: List[int]) -> bool:
        return count == [0] * 26

    def search(self, pat: str, txt: str) -> int:
        k = len(pat)
        count = [0] * 26
        for ch in pat:
            count[ord(ch) - ord('a')] += 1
        i = 0
        j = 0
        n = len(txt)
        result = 0
        while j < n:
            idx = ord(txt[j]) - ord('a')
            count[idx] -= 1

            if j - i + 1 == k:
                if self.allZero(count):
                    result += 1

                count[ord(txt[i]) - ord('a')] += 1
                i += 1
            j += 1
        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().search("for", "forxxorfxdofr") == 3
    assert Solution().search("abc", "abcbacab") == 4
    print("ok")
