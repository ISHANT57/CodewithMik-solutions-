# MY YOUTUBE VIDEO ON THIS Qn :
# Company Tags                : Paytm
# GfG Link                    : https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1

# Approach (Khandani Sliding Window template)
# T.C : O(n) -> No element is visited more than twice
# S.C : O(1)
from typing import List


class Solution:
    def smallestSubstring(self, s: str) -> int:
        n = len(s)

        i = 0
        j = 0

        result = 2**31 - 1  # INT_MAX
        zero = 0
        one = 0
        two = 0

        while j < n:
            if s[j] == '0':
                zero += 1
            elif s[j] == '1':
                one += 1
            else:
                two += 1

            while zero > 0 and one > 0 and two > 0 and j - i + 1 >= 3:
                result = min(result, j - i + 1)

                if s[i] == '0':
                    zero -= 1
                elif s[i] == '1':
                    one -= 1
                elif s[i] == '2':
                    two -= 1

                i += 1

            j += 1

        return -1 if result == 2**31 - 1 else result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().smallestSubstring("10212") == 3
    assert Solution().smallestSubstring("12121") == -1
    print("All tests passed")
