# Implement Queue class directly
class Queue():
    
    def __init__(self):
        
        self.queue = []
        
    def Enqueue(self, data):
        
        self.queue.append(data)
        
    def Dequeue(self):
        
        Dequeue_Data = None
        
        if self.IsEmpty():
            print("Queue is empty")
        
        else:
            Dequeue_Data = self.queue[0]
            self.queue = self.queue[1:]
            
        return Dequeue_Data
    
    def Peek(self):
        
        Peek_Data = None
        
        if self.IsEmpty():
            print("Queue is empty")
        
        else:
            Peek_Data = self.queue[0]
            
        return Peek_Data
    
    def IsEmpty(self):
        
        if len(self.queue) == 0:
            
            return True
        else :  return False

def BFS1(Graph,Start_Vertex):
    
    CV = Start_Vertex
    stack = Queue()
    history = [False]*len(Graph)
    stack.Enqueue(CV)
    history[CV] = True
    
    
    while stack.IsEmpty() != True :
        cv = stack.Dequeue()
        print(cv, end = ' ')
        for vertex in Graph[cv]:
            
            if history[vertex] == True: pass
        
            else:
                 
                 stack.Enqueue(vertex)
                 history[vertex] = True
    
if __name__ == "__main__":
    
    Graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]] # link information
    BFS1(Graph,1)