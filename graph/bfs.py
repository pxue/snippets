from collections import deque

def bfsl(graph, start, end):

    q = deque()
    q.append([start])

    while q:
        path = q.popleft()
        node = path[-1]

        if node == end:
            return path
        for edge in graph.get(node, []):
            new_path = list(path)
            new_path.append(edge)
            q.append(new_path)

def bfsl2(graph, start):

    q = deque()
    q.append(start)

    dist = {'1':0}
    while q:
        node = q.popleft()

        for edge in graph.get(node, []):
            if not dist.get(str(edge)):
                dist[edge] = dist[node] + 1
                q.append(edge)

    return dist

def bfsm2(graph, start):

    q = deque()
    q.append(start)
    dist = {1: 0}

    while q:
        node = q.popleft()
        for i,e in enumerate(graph[node-1], 1):
            if e == '0': continue
            if not dist.get(i):
                dist[i] = dist[node] + 1
                q.append(i)
    return dist


def bfsm(graph, start, end):

    q = deque()
    q.append([start])

    while q:
        path = q.popleft()

        node = path[-1]
        if node == end:
            return path
        for i,e in enumerate(graph[node-1], 1):
            if e == '0': continue
            new_path = list(path)
            new_path.append(i)
            q.append(new_path)



if __name__ == '__main__':

    graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

    adj_list = {}
    file = open('h3_al.txt')
    for i, x in enumerate(file, 1):
        adj_list[str(i)] = [z.strip() for z in x.split('    ')]
    file.close()

    adj_matrix = [] 
    file = open('h3_am.txt')
    for row in file:
        adj_matrix.append([x.strip() for x in row.split('\t')])
    file.close()

    #max_val = 0
    #for k, v in graph.iteritems():
        #max_val = max(max_val, int(k), int(max(v)))

    #matrix = []
    #for row in xrange(1, max_val):
        #temp = []
        #for col in xrange(1, max_val):
            #if row == col:
                #temp.append(1)
            #elif graph.get(str(row)) and str(col) in graph.get(str(row)):
                #temp.append(1)
            #else:
                #temp.append(0)
        #matrix.append(temp)

    #for row in xrange(0, max_val-1):
        #for col in xrange(0, max_val-1):
            #if matrix[row][col] == 1:
                #matrix[col][row] = 1

    #print "\n".join(["\t".join(map(str, r)) for r in matrix])


    #print bfsl2(graph, '1')
    print bfsl(adj_list, '1', '73')
    print bfsl2(adj_list, '1')['73']
    print bfsm2(adj_matrix, 1)

