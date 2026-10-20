# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=pqzvpK8zTHU
# Company Tags                : Google, Zoho, Flipkart,
# Leetcode Link               : https://leetcode.com/problems/reverse-vowels-of-a-string/
# GfG Link                    : https://practice.geeksforgeeks.org/problems/reversing-the-vowels5304/1


# Simply using  Two pointer technique
class Solution:
    def isVowel(self, ch: str) -> bool:
        return (ch == 'a' or ch == 'e' or
                ch == 'i' or ch == 'o' or
                ch == 'u' or
                ch == 'A' or ch == 'E' or
                ch == 'I' or ch == 'O' or
                ch == 'U')

    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)  # Python strings are immutable (C++ mutates s in place)
        i = 0
        j = n - 1

        while i < j:
            if not self.isVowel(s[i]):
                i += 1

            elif not self.isVowel(s[j]):
                j -= 1

            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().reverseVowels("IceCreAm") == "AceCreIm"
    assert Solution().reverseVowels("leetcode") == "leotcede"
    print("ok")
