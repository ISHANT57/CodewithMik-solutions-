# MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=6zq1BBMAam0
# Company Tags                : GOOGLE
# Leetcode Link               : https://leetcode.com/problems/reconstruct-itinerary/

import heapq
from typing import List
from collections import defaultdict


# Approach-1 (Using adj of string to vector and sorting it)
# T.C : O(V^2)
class Solution:
    def __init__(self):
        self.adj = defaultdict(list)
        self.route = []
        self.numTickets = 0

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = defaultdict(list)
        self.route = []
        self.numTickets = len(tickets)

        for t in tickets:
            u = t[0]
            v = t[1]

            self.adj[u].append(v)

        # Sort vertices in the adjacency list by lexical order
        for key in list(self.adj.keys()):
            self.adj[key].sort()

        temp = []
        self.DFS("JFK", temp)
        return self.route

    def DFS(self, fromAirport: str, temp: List[str]) -> bool:
        temp.append(fromAirport)

        # we have used all tickets, this is a valid path return the result
        if len(temp) == self.numTickets + 1:
            self.route = temp[:]
            return True

        # You have already found the route (first valid lexicographically path)

        neighbors = self.adj[fromAirport]

        # at the current layer, try its neighbors in the sorted order
        i = 0
        while i < len(neighbors):
            toAirport = neighbors[i]

            # remove ticket(route) from graph so that it won't be reused
            neighbors.pop(i)

            if self.DFS(toAirport, temp):
                return True

            # if the current path is invalid, restore the current ticket
            neighbors.insert(i, toAirport)
            i += 1

        temp.pop()
        return False


Approach1 = Solution


# Approach-2 (Using adj of string to min-heap)
class Solution:
    def __init__(self):
        # priority_queue<string, vector<string>, greater<string>> -> min-heap via heapq
        self.adj = defaultdict(list)
        self.result = []

    def dfs(self, u: str) -> None:
        edges = self.adj[u]

        while edges:
            v = heapq.heappop(edges)
            self.dfs(v)
        self.result.append(u)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj = defaultdict(list)
        self.result = []
        for e in tickets:
            heapq.heappush(self.adj[e[0]], e[1])

        self.dfs("JFK")
        self.result.reverse()
        return self.result


Approach2 = Solution

# (Java section of the original file skipped: duplicate of Approach-1)

if __name__ == "__main__":
    for S in (Approach1, Approach2):
        assert S().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"]
        assert S().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    print("ok")
