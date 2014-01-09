import heapq
import time

start = time.clock()

f = open("Problem81.txt")
problem = []
curr = f.readline()
while curr:
    problem.append([int(i) for i in curr.split(",")])
    curr = f.readline()

def dijkstra(problem, start):
    dist = {}
    prev = {}
    q = []
    for i in range(80):
        for j in range(80):
            dist[(i, j)] = float("inf")
            prev[(i, j)] = None
            q.append((dist[(i, j)], (i, j)))
    heapq.heapify(q)
    dist[start] = problem[start[0]][start[1]]

    while q:
        u = heapq.heappop(q)[1]
        if dist[u] == float("inf"):
            break

        for v in ((u[0]+1, u[1]), (u[0], u[1]+1)):
            if v[0] < 80 and v[1] < 80:
                alt = dist[u] + problem[v[0]][v[1]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(q, ((dist[v], v)))

    return dist

print dijkstra(problem, (0, 0))[(79, 79)]
print time.clock() - start
