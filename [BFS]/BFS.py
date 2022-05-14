from collections import deque
Graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] # link information

def BFS(Graph, Start):
    
    queue = deque()
    queue.append(Start)
    history = [False]*len(Graph)
    history[Start] = True
    while queue:
        
        vertex = queue.popleft()
        print(vertex, end= '')
        
        for v in Graph[vertex]:
            if history[v] == True: pass
            else:
                queue.append(v)
                history[v] = True
BFS(Graph, 1)
