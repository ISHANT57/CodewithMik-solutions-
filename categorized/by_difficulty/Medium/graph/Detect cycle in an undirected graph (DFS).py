# Company Tags  : Flipkart, Amazon, Samsung, MakeMyTrip, Oracle, Adobe
# Question Link : https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List


def isCycleUtil(g: List[List[int]], start: int, visited: List[bool], parent: int) -> bool:
    visited[start] = True

    for it in g[start]:
        if it == parent:
            continue
        if visited[it] == True:
            return True
        if isCycleUtil(g, it, visited, start):
            return True

    return False


def isCyclic(g: List[List[int]], V: int) -> bool:
    visited = [False] * V

    for i in range(V):
        if visited[i] == False and isCycleUtil(g, i, visited, -1):
            return True
    return False


Approach1 = isCyclic


if __name__ == "__main__":
    assert isCyclic([[1, 2], [0, 2], [0, 1]], 3) == True
    assert isCyclic([[1], [0, 2], [1]], 3) == False
    print("ok")
