# Not recursive
def DFS1(Graph,Start_Vertex):
    
    CV = Start_Vertex
    stack = [0] # Put zero to prevent stack empty in the middle
    history = [False] * len(Graph)
    stack.append(CV)
    history[CV] = True
    print(CV, end = ' ')
    
    while len(stack) != 0:
        
        NV = None # Next vertex
        
        for vertex in Graph[CV]:
            
            if history[vertex] == True: pass
            else:
                NV = vertex
                break
            
        if NV != None:
            
            CV = NV
            history[CV] = True
            stack.append(CV)
            print(CV, end = ' ')
            
        else: CV = stack.pop()
                
# Recursive
def DFS2(Graph, Start_Vertex, history2):
    
    CV = Start_Vertex
    history2[CV] = True
    print(CV, end = ' ')
    
    for vertex in Graph[CV]:
        
        if not history2[vertex]:
            DFS2(Graph, vertex, history2)

if __name__ == "__main__":
    
    Graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] # link information
    DFS1(Graph, 1) # Not Recursive
    print('<- Not Recursive Result ')
    
    
    history2 = history = [False] * len(Graph)
    DFS2(Graph, 1, history2) # Recursive
    print('<- Recursive Result')