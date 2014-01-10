import heapq
import time

start = time.clock()

f = open("Problem82.txt")
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
            if (i, j) == start:
                dist[(i, j)] = problem[i][j]
            else:
                dist[(i, j)] = float("inf")
            prev[(i, j)] = None
            q.append((dist[(i, j)], (i, j)))
    heapq.heapify(q)

    while q:
        u = heapq.heappop(q)[1]
        if dist[u] == float("inf"):
            break

        for v in ((u[0]+1, u[1]), (u[0], u[1]-1), (u[0], u[1]+1)):
            if v[0] < 80 and v[1] < 80 and v[1] >= 0:
                alt = dist[u] + problem[v[0]][v[1]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(q, (dist[v], v))

    return dist

smallest = []
for i in range(80):
    curr = dijkstra(problem, (0, i))
    points = []
    for j in range(80):
        points.append(curr[79, j])
    smallest.append(min(points))
print min(smallest)
print time.clock() - start
