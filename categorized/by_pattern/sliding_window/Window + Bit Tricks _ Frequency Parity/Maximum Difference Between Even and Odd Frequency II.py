# Scroll below to see JAVA code also (Java section skipped in this Python port)
# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=zNi7uftAYEs
# Company Tags                : will update soon
# Leetcode Link               : https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii

INT_MIN = -2**31
INT_MAX = 2**31 - 1


# Approach  (Sliding Window)
# T.C : O(20 * n) ~= O(n)
# S.C : O(1)
class Solution:
    def getState(self, count_a: int, count_b: int) -> int:
        parity_a = count_a % 2  # odd : parity will be 1 , even : parity will be 0
        parity_b = count_b % 2

        if parity_a == 0 and parity_b == 0: return 0  # even even (00)
        if parity_a == 0 and parity_b == 1: return 1  # even odd (01)
        if parity_a == 1 and parity_b == 0: return 2  # odd even (10)

        return 3  # odd odd (11)

    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)

        result = INT_MIN

        # Step-1 Try all possible pairs a and b from ('0' to '4') where a != b
        for a in "01234":
            for b in "01234":
                if a == b:
                    continue

                # stateMinPrev_a_b[state] = stores the smallest value of count of a - count of b
                stateMinPrev_a_b = [INT_MAX] * 4

                # Count of a and count of b till index r
                count_a = 0
                count_b = 0

                # Count of a and count of b till prev index l
                prev_a = 0
                prev_b = 0

                # Let's start the sliding window
                l = -1
                r = 0

                while r < n:
                    count_a += 1 if s[r] == a else 0
                    count_b += 1 if s[r] == b else 0

                    # Now try to shrink from l
                    while r - l >= k and count_b - prev_b >= 2 and count_a - prev_a >= 1:
                        leftState = self.getState(prev_a, prev_b)
                        stateMinPrev_a_b[leftState] = min(stateMinPrev_a_b[leftState], prev_a - prev_b)

                        l += 1
                        prev_a += 1 if s[l] == a else 0
                        prev_b += 1 if s[l] == b else 0

                    rightState = self.getState(count_a, count_b)
                    bestLeftState = rightState ^ 2
                    bestMinDiffValueLeft = stateMinPrev_a_b[bestLeftState]

                    if bestMinDiffValueLeft != INT_MAX:
                        result = max(result, (count_a - count_b) - bestMinDiffValueLeft)

                    r += 1

        return result


Approach1 = Solution


if __name__ == "__main__":
    assert Solution().maxDifference("12233", 4) == -1
    assert Solution().maxDifference("1122211", 3) == 1
    assert Solution().maxDifference("110", 3) == -1
    print("all tests passed")
