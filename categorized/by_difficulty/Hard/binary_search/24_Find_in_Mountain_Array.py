# MY YOUTUBE VIDEO ON THIS QN : https://www.youtube.com/watch?v=wzHmgBIdQXA
# Company Tags                : AMAZON
# Leetcode Link               : https://leetcode.com/problems/find-in-mountain-array/

# You can see my video on finding "Peak Index in a Mountain Array" -
#     Code Link - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/Arrays/Binary%20Search/Peak%20Index%20in%20a%20Mountain%20Array.cpp
#     YouTube Video Link - https://www.youtube.com/watch?v=Op07kT-LoH8

# (Java section of the original is not ported: this file is the Python 3 port of the C++ code)


# Mock of LeetCode's MountainArray interface (LeetCode provides this itself)
class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


# ********************************************************* C++ (ported to Python) **************************************************************
# Approach - Solving using Binary Search
# T.C : log(n)
# S.C : O(1)
class Solution:
    # This function is already taught in my YouTube Video - https://www.youtube.com/watch?v=Op07kT-LoH8 ("Peak Index in a Mountain Array")
    def peakIndexInMountainArray(self, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l = 0
        r = n - 1

        while l < r:

            mid = l + (r - l) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid

        return l

    def binarySearch(self, mountainArr: 'MountainArray', l: int, r: int, target: int) -> int:

        while l <= r:
            mid = l + (r - l) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

    def reverseBinarySearch(self, mountainArr: 'MountainArray', l: int, r: int, target: int) -> int:
        while l <= r:
            mid = l + (r - l) // 2

            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:  # Because the array in right side of peak is in descending order
                l = mid + 1
            else:
                r = mid - 1

        return -1

    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        peakIndex = self.peakIndexInMountainArray(mountainArr)

        idx = self.binarySearch(mountainArr, 0, peakIndex, target)

        if idx == -1:
            return self.reverseBinarySearch(mountainArr, peakIndex, n - 1, target)

        return idx


if __name__ == "__main__":
    s = Solution()
    assert s.findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2
    assert s.findInMountainArray(3, MountainArray([0, 1, 2, 4, 2, 1])) == -1
    assert s.findInMountainArray(1, MountainArray([1, 5, 2])) == 0
    print("ok")
