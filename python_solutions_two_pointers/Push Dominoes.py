# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=HrUZKTzStII
# Company Tags                : Google, Microsoft
# Leetcode Link               : https://leetcode.com/problems/push-dominoes/

from typing import List


# Approach-1
# T.C : (O(n) time : Finding closest 'L' and closest 'R')
# S.C : O(n)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)

        rightClosestL = [0] * n
        leftClosestR = [0] * n

        # Moving right to left to find rightClosestL
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                rightClosestL[i] = i  # L starts from me
            elif dominoes[i] == '.':
                rightClosestL[i] = rightClosestL[i + 1] if i < n - 1 else -1
            else:
                rightClosestL[i] = -1

        # Moving left to right to find leftClosestR
        for i in range(n):
            if dominoes[i] == 'R':
                leftClosestR[i] = i  # R starts from me
            elif dominoes[i] == '.':
                leftClosestR[i] = leftClosestR[i - 1] if i > 0 else -1
            else:
                leftClosestR[i] = -1

        result = [' '] * n

        for i in range(n):
            distRightL = abs(i - rightClosestL[i])  # distance from 'R' towards my left direction
            distLeftR = abs(i - leftClosestR[i])    # distance from 'L' towards my right direction

            if rightClosestL[i] == leftClosestR[i]:
                result[i] = '.'
            elif rightClosestL[i] == -1:   # No force from right direction towards left, so move R
                result[i] = 'R'
            elif leftClosestR[i] == -1:    # No force from left direction towards right, so move L
                result[i] = 'L'
            elif distLeftR == distRightL:  # Equal force from left and right
                result[i] = '.'
            else:
                result[i] = 'L' if distRightL < distLeftR else 'R'  # which ever force is greater (either from left by 'R' or from right by 'L')

        return "".join(result)


Approach1 = Solution


# Approach-2
# T.C : (O(n) time : Using Force Simulation)
# S.C : O(n)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)

        forces = [0] * n

        # Move from left to right and look for right force 'R'
        force = 0  # initially
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # My max power towards Right starts from here and it will decrease as I progress
            elif dominoes[i] == 'L':
                force = 0  # I can't give force towards Right :-(
            else:
                force = max(force - 1, 0)  # I told ya, my power decreases as I progress and hit a '.'

            forces[i] = force

        # Move from right to left and look for left force 'L'
        force = 0  # initially
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n  # My max power towards Left starts from here and it will decrease as I progress
            elif dominoes[i] == 'R':
                force = 0  # I can't give force towards Left :-(
            else:
                force = max(force - 1, 0)  # I told ya, my power decreases as I progress and hit a '.'

            forces[i] -= force  # resultant force (that's why I am subtracting)

        # Now I will find resultant direction on each domino basis of resultant force on them
        result = ['.'] * n
        for i in range(n):
            if forces[i] < 0:
                result[i] = 'L'
            elif forces[i] > 0:
                result[i] = 'R'
        return "".join(result)


Approach2 = Solution


# Approach-3
# T.C : (O(n) time : Two Pointer Technique)
# S.C : O(n), extra s taken
"""
	In this approach, you just need to find sections like this
	X .   .   .   . X
	i                j
	Where X can be 'R' or 'L' and in between there can be as many dots
	Now,
	- you know the length of mid part
	- If char[i] == char[j] == 'R', means all go towards right (R)
	-  char[i]  == char[j] == 'L', means all go towards Left (L)
	-  If char[i] = 'L' and char[j] = 'R', means middle part is not affected so the remain '.'
	-  If char[i] = 'R' and char[j] = 'L', then it will affect the middle part.
	   The middle_part/2 close to i will be affected by 'R' and middle_part/2 close to j will be
	   effected by 'L'  and the last mid point (middle_part%2) will be unaffected due to equal
	   force from left and right so it remains '.'
"""
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = "L" + dominoes + "R"
        n = len(s)
        result = ""
        i = 0
        for j in range(1, n):
            if s[j] == '.':
                continue

            midPartLength = j - i - 1
            if i > 0:
                result += s[i]

            if s[i] == s[j]:
                result += s[i] * midPartLength
            elif s[i] == 'L' and s[j] == 'R':
                result += '.' * midPartLength
            else:
                result += 'R' * (midPartLength // 2) + '.' * (midPartLength % 2) + 'L' * (midPartLength // 2)
            i = j

        return result


Approach3 = Solution


if __name__ == "__main__":
    for A in (Approach1, Approach2, Approach3):
        assert A().pushDominoes("RR.L") == "RR.L"
        assert A().pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
    print("ok")
