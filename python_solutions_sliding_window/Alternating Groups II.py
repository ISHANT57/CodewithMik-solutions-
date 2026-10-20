# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=EZVLzXvaQ2A
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/alternating-groups-ii/description/

from typing import List

# Approach-1 (Brute Force)
# T.C : O(n*k)
# S.C : O(1)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        for i in range(k - 1):
            colors.append(colors[i])

        result = 0
        for i in range(n):
            isAlternating = True
            for j in range(i, i + k - 1):
                if colors[j] == colors[j + 1]:
                    isAlternating = False
                    break
            if isAlternating:
                result += 1

        return result


Approach1 = Solution


# Approach-2 (Sliding Window using Khandani Template)
# T.C : O(n+k)
# S.C : O(1) (But you can mention you have to add k-1 extra elements so space complexity ideally should be O(k-1))
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        N = n + (k - 1)
        for i in range(k - 1):
            colors.append(colors[i])  # to handle wrap around (circular array)

        result = 0
        i = 0
        j = 1  # because we have to check index j-1 for checking alterate
        while j < N:
            if colors[j] == colors[j - 1]:
                i = j
                j += 1
                continue

            if j - i + 1 == k:
                result += 1
                i += 1

            j += 1

        return result


Approach2 = Solution


# Approach-3 (Using simple counting in 2 Pass)
# T.C : O(n+k)
# S.C : O(1)
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        result = 0

        length = 1  # i = 0 index wala element
        last = colors[0]
        # 1st Pass
        for i in range(1, n):
            if colors[i] == last:
                length = 1
                last = colors[i]
                continue

            length += 1

            if length >= k:
                result += 1

            last = colors[i]

        # T.C : O(n)
        # 2nd Pass
        for i in range(k - 1):  # checking starting (k-1) elements
            if colors[i] == last:
                length = 1
                last = colors[i]
                break

            length += 1

            if length >= k:
                result += 1

            last = colors[i]

        return result


Approach3 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2, Approach3):
        assert S().numberOfAlternatingGroups([0, 1, 0, 1, 0], 3) == 3
        assert S().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6) == 2
        assert S().numberOfAlternatingGroups([1, 1, 0, 1], 4) == 0
    print("ok")
