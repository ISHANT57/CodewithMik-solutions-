# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=2d1ALG8wwDc
# Company Tags                : Will update soon
# Leetcode Link -
# Count Substrings That Satisfy K-Constraint I  : https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i
# Count Substrings That Satisfy K-Constraint II : https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii

from typing import List
from collections import defaultdict


############################ "Count Substrings That Satisfy K-Constraint I" ############################
# Approach-1 (Using Brute Force)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)

        result = 0

        for i in range(n):

            count0 = 0
            count1 = 0

            for j in range(i, n):
                if s[j] == '0':
                    count0 += 1
                else:
                    count1 += 1

                if count0 <= k or count1 <= k:
                    result += 1
                else:
                    break

        return result


Approach1 = Solution


############################ "Count Substrings That Satisfy K-Constraint I" ############################
# Approach-2 (Using Sliding Window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)

        result = 0

        count0 = 0
        count1 = 0

        i = 0
        j = 0

        # T.C : O(n)
        while j < n:
            if s[j] == '0':
                count0 += 1
            else:
                count1 += 1

            while count0 > k and count1 > k:  # unsatisfied window, keep shrinking
                if s[i] == '0':
                    count0 -= 1
                else:
                    count1 -= 1
                i += 1

            result += (j - i + 1)
            j += 1

        return result


Approach2 = Solution


############################ "Count Substrings That Satisfy K-Constraint II" ############################
# (Using Sliding Window and cumulative sum)
# T.C : O(n + Q), where n = s.length and Q = number of queries
# S.C : O(n)
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)

        leftMost = [0] * n
        rightMost = [0] * n

        # leftMost[j] = i; # For index j, what is the left most valid index i until which we get valid substring
        i = 0
        j = 0
        mp = defaultdict(int)  # unordered_map<char, int>

        while j < n:
            mp[s[j]] += 1
            while mp['0'] > k and mp['1'] > k:
                mp[s[i]] -= 1
                i += 1

            leftMost[j] = i
            j += 1

        # rightMost[j] = i; # For index j, what is the right most valid index until which we get valid substring
        mp.clear()
        i = n - 1
        j = n - 1
        while j >= 0:
            mp[s[j]] += 1
            while mp['0'] > k and mp['1'] > k:
                mp[s[i]] -= 1
                i -= 1
            rightMost[j] = i
            j -= 1

        # tempValidSubstr[j] = number of valid substrings ending at index j
        tempValidSubstr = [0] * n
        for j in range(n):
            tempValidSubstr[j] = j - leftMost[j] + 1

        # cumSum
        cumSum = [0] * n
        cumSum[0] = tempValidSubstr[0]
        for i in range(1, n):
            cumSum[i] = cumSum[i - 1] + tempValidSubstr[i]

        result = []
        for query in queries:
            low = query[0]
            high = query[1]

            validRightIdx = min(high, rightMost[low])

            length = validRightIdx - low + 1

            tempResult = length * (length + 1) // 2

            tempResult += cumSum[high] - cumSum[validRightIdx]

            result.append(tempResult)

        return result


Approach3 = Solution


if __name__ == "__main__":
    assert Approach1().countKConstraintSubstrings("10101", 1) == 12
    assert Approach1().countKConstraintSubstrings("1010101", 2) == 25
    assert Approach1().countKConstraintSubstrings("11111", 1) == 15
    assert Approach2().countKConstraintSubstrings("10101", 1) == 12
    assert Approach2().countKConstraintSubstrings("1010101", 2) == 25
    assert Approach2().countKConstraintSubstrings("11111", 1) == 15
    assert Approach3().countKConstraintSubstrings("0001111", 2, [[0, 6]]) == [26]
    assert Approach3().countKConstraintSubstrings("010101", 1, [[0, 5], [1, 4], [2, 3]]) == [15, 9, 3]
    print("ok")
