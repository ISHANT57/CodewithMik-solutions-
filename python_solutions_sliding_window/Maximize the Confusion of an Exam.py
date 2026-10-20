# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=vY06L8hZVGI
# Company Tags                : MICROSOFT
# Leetcode Link               : https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
# Similar Leetcode Problem    : https://leetcode.com/problems/max-consecutive-ones-iii/

from collections import defaultdict


# Approach-1 (Simple Brute Force) - O(n * 2^n)
class Solution:
    def findMax(self, answerKey):
        # answerKey is a list of chars (mutable, mirrors C++ string &)
        length = 0

        i = 0

        while i < self.n:

            if answerKey[i] == 'T':
                length = 1
                i += 1
                while i < self.n and answerKey[i] == 'T':
                    length += 1
                    i += 1
                self.ans = max(self.ans, length)
            else:
                length = 1
                i += 1
                while i < self.n and answerKey[i] == 'F':
                    length += 1
                    i += 1
                self.ans = max(self.ans, length)

    def solve(self, idx, answerKey, k):

        self.findMax(answerKey)

        if idx >= self.n or k <= 0:
            return

        answerKey[idx] = 'F' if answerKey[idx] == 'T' else 'T'  # Flipped

        self.solve(idx + 1, answerKey, k - 1)

        answerKey[idx] = 'F' if answerKey[idx] == 'T' else 'T'  # Flipped back
        self.solve(idx + 1, answerKey, k)

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        self.ans = 0
        self.n = len(answerKey)

        self.solve(0, list(answerKey), k)

        return self.ans


Approach1 = Solution


# Approach-2 (Using a Sliding Window twice)
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        result = 0
        # First pass for flipping 'F' -> 'T'

        i, j = 0, 0
        countF = 0
        while j < n:
            if answerKey[j] == 'F':
                countF += 1

            while countF > k:
                if answerKey[i] == 'F':
                    countF -= 1
                i += 1

            result = max(result, j - i + 1)

            j += 1

        i, j = 0, 0
        countT = 0
        while j < n:
            if answerKey[j] == 'T':
                countT += 1

            while countT > k:
                if answerKey[i] == 'T':
                    countT -= 1
                i += 1

            result = max(result, j - i + 1)
            j += 1

        return result


Approach2 = Solution


# Approach-3 (Using One Pass Sliding Window)
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = k

        mp = defaultdict(int)  # unordered_map<char, int>

        i = 0
        for j in range(len(answerKey)):

            mp[answerKey[j]] += 1

            while min(mp['T'], mp['F']) > k:
                mp[answerKey[i]] -= 1
                i += 1

            result = max(result, j - i + 1)

        return result


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().maxConsecutiveAnswers("TTFF", 2) == 4
        assert S().maxConsecutiveAnswers("TFFT", 1) == 3
        assert S().maxConsecutiveAnswers("TTFTTFTT", 1) == 5
    print("all tests passed")
