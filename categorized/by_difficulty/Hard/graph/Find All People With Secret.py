#                        Scroll down to see JAVA code also (Java sections skipped in this Python port)
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=hxEWwnJJKcY
#     Company Tags                : GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/find-all-people-with-secret/

from typing import List
from collections import defaultdict, deque
import heapq

INT_MAX = 2**31 - 1


# ********************************************************************** C++ (ported to Python) **********************************************************************
# Approach-1 (Most basic approach that can come to mind)
# T.C : ~O(M*(M+N)) where M = number of meetings and N = number of people
# S.C : O(M+N)
class Solution:
    # typedef pair<int, int> P;  -> tuple
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        timeMeetings = defaultdict(list)  # map<int, vector<P>> : ordered by key, so iterate over sorted(keys)

        for meeting in meetings:
            person1 = meeting[0]
            person2 = meeting[1]
            time = meeting[2]

            timeMeetings[time].append((person1, person2))

        knowsSecret = [False] * n
        knowsSecret[0] = True
        knowsSecret[firstPerson] = True

        # Solve in increasing time meetings
        for t in sorted(timeMeetings):

            meets = timeMeetings[t]

            adj = defaultdict(list)
            que = deque()
            alreadyAdded = set()

            for person1, person2 in meets:
                adj[person1].append(person2)
                adj[person2].append(person1)

                if knowsSecret[person1] and person1 not in alreadyAdded:
                    que.append(person1)
                    alreadyAdded.add(person1)
                if knowsSecret[person2] and person2 not in alreadyAdded:
                    que.append(person2)
                    alreadyAdded.add(person2)

            # Now I know who meet who based on increasing time
            # Let's hit the BFS to spread the secret

            while que:
                person = que.popleft()

                for nextPerson in adj[person]:
                    if not knowsSecret[nextPerson]:
                        knowsSecret[nextPerson] = True
                        que.append(nextPerson)

        result = []
        for i in range(n):
            if knowsSecret[i] == True:
                result.append(i)

        return result


Approach1 = Solution


# Approach-2 (Using BFS Graph Traversal)
# T.C : O(M * (M+N)) -> M = Number of meetings, N = number of people, there can be at most N+M elements in the queue and a person may have M neighbours
# S.C : O(M+N)
class Solution:
    # typedef pair<int, int> P;  -> tuple
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)

        for meeting in meetings:
            person1 = meeting[0]
            person2 = meeting[1]
            time = meeting[2]

            adj[person1].append((person2, time))
            adj[person2].append((person1, time))

        que = deque()
        que.append((0, 0))
        que.append((firstPerson, 0))
        earlySecretTime = [INT_MAX] * n
        earlySecretTime[0] = 0
        earlySecretTime[firstPerson] = 0

        while que:
            person, time = que.popleft()

            for ngbr in adj[person]:
                nextPerson = ngbr[0]
                t = ngbr[1]

                if t >= time and earlySecretTime[nextPerson] > t:
                    earlySecretTime[nextPerson] = t
                    que.append((nextPerson, t))

        result = []
        for i in range(n):
            if earlySecretTime[i] != INT_MAX:
                result.append(i)

        return result


Approach2 = Solution


# Approach-3 (Using DFS Graph Traversal)
# T.C : O(M * (M+N)) -> M = Number of meetings, N = number of people (Although it's a DFS, but we also revisit some nodes again with better secret knowing time)
# S.C : O(M+N)
class Solution:
    # typedef pair<int, int> P;  -> tuple

    def dfs(self, person: int, time: int, adj, earlySecretTime: List[int]) -> None:
        for ngbr in adj[person]:
            nextPerson = ngbr[0]
            t = ngbr[1]

            if t >= time and earlySecretTime[nextPerson] > t:
                earlySecretTime[nextPerson] = t
                self.dfs(nextPerson, t, adj, earlySecretTime)

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)

        for meeting in meetings:
            person1 = meeting[0]
            person2 = meeting[1]
            time = meeting[2]

            adj[person1].append((person2, time))
            adj[person2].append((person1, time))

        earlySecretTime = [INT_MAX] * n
        earlySecretTime[0] = 0
        earlySecretTime[firstPerson] = 0

        # Do DFS
        self.dfs(0, 0, adj, earlySecretTime)
        self.dfs(firstPerson, 0, adj, earlySecretTime)

        result = []
        for i in range(n):
            if earlySecretTime[i] != INT_MAX:
                result.append(i)

        return result


Approach3 = Solution


# Approach-4 (Using min-heap to fetch earliest time)
# T.C : ~O((N+M) * (log(M+N) + M))
# S.C : O(N+M)
class Solution:
    # typedef pair<int, int> P;  -> tuple
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = defaultdict(list)

        for meeting in meetings:
            person1 = meeting[0]
            person2 = meeting[1]
            time = meeting[2]

            adj[person1].append((person2, time))
            adj[person2].append((person1, time))

        pq = []  # priority_queue<P, vector<P>, greater<P>> -> heapq is a min-heap already
        # I need the ones first having min time
        heapq.heappush(pq, (0, 0))
        heapq.heappush(pq, (0, firstPerson))

        visited = [False] * n

        while pq:
            time, person = heapq.heappop(pq)

            if visited[person] == True:
                continue
            visited[person] = True

            for ngbr in adj[person]:
                nextPerson = ngbr[0]
                t = ngbr[1]

                if t >= time and not visited[nextPerson]:
                    heapq.heappush(pq, (t, nextPerson))

        result = []
        for i in range(n):
            if visited[i] == True:
                result.append(i)

        return result


Approach4 = Solution


if __name__ == "__main__":
    for cls in (Approach1, Approach2, Approach3, Approach4):
        assert cls().findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1) == [0, 1, 2, 3, 5]
        assert cls().findAllPeople(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3) == [0, 1, 3]
        assert cls().findAllPeople(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1) == [0, 1, 2, 3, 4]
    print("ok")
