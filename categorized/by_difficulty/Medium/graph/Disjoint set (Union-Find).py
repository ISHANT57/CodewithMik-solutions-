# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=AsAdKHkITBQ
# Company Tags                : Google, Facebook, Apple, Amazon, Netflix, Flipkart
# GfG Link                    : https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1

from typing import List


# Complete the functions below
def find(A: List[int], x: int) -> int:
    if A[x] == x:
        return x

    A[x] = find(A, A[x])  # This is Path compression
    return A[x]


def unionSet(A: List[int], X: int, Z: int) -> None:
    x = find(A, X)
    y = find(A, Z)

    if x == y:
        return

    A[x] = y


if __name__ == "__main__":
    A = list(range(5))
    unionSet(A, 0, 1)
    unionSet(A, 2, 3)
    assert find(A, 0) == find(A, 1)
    assert find(A, 0) != find(A, 2)
    unionSet(A, 1, 3)
    assert find(A, 0) == find(A, 2)
    assert find(A, 4) == 4
    print("ok")
