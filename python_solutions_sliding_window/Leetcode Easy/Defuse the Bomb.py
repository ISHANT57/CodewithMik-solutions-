from typing import List

#     MY YOUTUBE VIDEO ON THIS Qn   : https://www.youtube.com/watch?v=QjO6T1cThRU
#     Company Tags                  : Will update soon
#     Leetcode Link                 : https://leetcode.com/problems/defuse-the-bomb


# **************************************************************** C++ ****************************************************************
# Approach-1 (Brute Force)
# T.C : O(n*|k|)
# S.C : O(1)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        result = [0] * n
        if k == 0:
            return result

        for i in range(n):
            if k < 0:
                for j in range(i - abs(k), i):
                    result[i] += code[(j + n) % n]
            else:
                for j in range(i + 1, i + k + 1):
                    result[i] += code[j % n]
        return result


Approach1 = Solution


# Approach-2 (Sliding Window)
# T.C : O(n)
# S.C : O(1)
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        result = [0] * n
        if k == 0:
            return result  # {0, 0, 0,...}

        i = -1
        j = -1
        if k > 0:
            i = 1
            j = k
        else:
            i = n - abs(k)
            j = n - 1

        windowSum = 0
        for pointer in range(i, j + 1):
            windowSum += code[pointer]

        for k in range(n):  # result[k]
            result[k] = windowSum

            windowSum -= code[i % n]
            i += 1

            windowSum += code[(j + 1) % n]
            j += 1

        return result


Approach2 = Solution


if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
        assert S().decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
        assert S().decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
    print("All tests passed")
