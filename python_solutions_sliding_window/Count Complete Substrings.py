# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ygPMLjxaT2Y
# Company Tags                : Soon will update
# Leetcode Link               : https://leetcode.com/problems/count-complete-substrings/description/

# Approach (Using sliding window)
# T.C : O(n*26*n) ~ O(n^2)
# S.C : O(26) We create an array of size 26 everytime. So assuming it constant
class Solution:
    def solve(self, start: int, end: int, word: str, k: int) -> int:
        result = 0
        chars = 1
        while chars <= 26 and chars * k <= end - start + 1:

            count = [0] * 26
            goodChars = 0  # How many chars are of frequency k

            # Now do a sliding window
            i = start
            windowLength = chars * k
            for j in range(start, end + 1):
                ch = word[j]

                count[ord(ch) - ord('a')] += 1
                if count[ord(ch) - ord('a')] == k:
                    goodChars += 1
                elif count[ord(ch) - ord('a')] == k + 1:
                    goodChars -= 1

                if j - i + 1 > windowLength:  # Need to shift window right
                    if count[ord(word[i]) - ord('a')] == k:
                        goodChars -= 1
                    elif count[ord(word[i]) - ord('a')] == k + 1:
                        goodChars += 1
                    count[ord(word[i]) - ord('a')] -= 1
                    i += 1

                if goodChars == chars:
                    result += 1

            chars += 1

        return result

    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        result = 0
        last = 0

        for i in range(1, n + 1):
            if i == n or abs(ord(word[i]) - ord(word[i - 1])) > 2:  # satisying condition 2
                result += self.solve(last, i - 1, word, k)  # condition 1
                last = i

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().countCompleteSubstrings("igigee", 2) == 3
    assert Solution().countCompleteSubstrings("aaabbbccc", 3) == 6
    print("ok")
