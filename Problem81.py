import Queue

f = open("Problem81.txt")
problem = []
curr = f.readline()
while curr:
    problem.append([int(i) for i in curr.split(",")])
    curr = f.readline()

def uniformCostSearch(problem):
    closed = set()
    fringe = Queue.PriorityQueue()
    fringe.put((0, (0, 0)))
    while not fringe.empty():
        item = fringe.get()
        if item[1] == (len(problem)-1, len(problem[0])-1):
            return problem[item[1][0]][item[1][1]]
        if item[1] not in closed:
            closed.add(item)
            if item[1][0] < len(problem)-1:
                fringe.put((item[0] + problem[item[1][0]][item[1][1]], (item[1][0]+1, item[1][1])))
            if item[1][1] < len(problem[0])-1:
                fringe.put((item[0] + problem[item[1][0]][item[1][1]], (item[1][0], item[1][1]+1)))

print uniformCostSearch(problem)
