def Dijkstra(start_node):
    stack = [0]*n
    current_node = start_node
    history[current_node] = True
    distance[current_node] = 0
    stack.pop()
    
    for i in graph[current_node]:
        distance[i[0]] = i[1]
        
    while len(stack) != 0:
        
        current_node = Default_value
        for i in range(1,n+1):
            if not history[i] and distance[i] < current_node: current_node = i
        
        history[current_node] = True
        stack.pop()
        
        for i in graph[current_node]:
            cost = distance[current_node] + i[1]
            if cost < distance[i[0]]: distance[i[0]] = cost
            
    return distance
'''   
if __name__ == "__main__":
    
    Default_value = 99
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n+1)]
    history = [False]*(n+1)
    distance = [Default_value]*(n+1)
    for _ in range(m):    
        a, b, c =  map(int, input().split())
        graph[a].append((b,c)) 
    print(Dijkstra(1))
'''