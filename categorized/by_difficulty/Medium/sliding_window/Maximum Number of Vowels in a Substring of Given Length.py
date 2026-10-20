# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=CAVnGkDzqAs
# Company Tags                : MICROSOFT
# Leetcode Link               : https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


# Sliding window - Separate function to check vowel
class Solution:
    def isVowel(self, ch: str) -> bool:
        return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        maxV = 0
        count = 0
        i, j = 0, 0

        while j < n:

            if self.isVowel(s[j]):
                count += 1

            if j - i + 1 == k:
                maxV = max(maxV, count)
                if self.isVowel(s[i]):
                    count -= 1
                i += 1

            j += 1

        return maxV


Approach1 = Solution


# Sliding Window - Writing a lambda function to check vowel
class Solution:

    def maxVowels(self, s: str, k: int) -> int:

        isVowel = lambda ch: ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'

        n = len(s)

        maxV = 0
        count = 0
        i, j = 0, 0

        while j < n:

            if isVowel(s[j]):
                count += 1

            if j - i + 1 == k:
                maxV = max(maxV, count)
                if isVowel(s[i]):
                    count -= 1
                i += 1

            j += 1

        return maxV


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().maxVowels("abciiidef", 3) == 3
        assert S().maxVowels("aeiou", 2) == 2
        assert S().maxVowels("leetcode", 3) == 2
    print("all tests passed")
