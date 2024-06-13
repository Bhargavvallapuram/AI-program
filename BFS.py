from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def BFS(self,start,goal):
        if(start==goal):
            return True
        for node in self.graph[start]:
            
            if(self.BFS(node,goal)):
                return True
        return False
    def BFSTraversal(self,s):
        queue=[s]
        visit=[False]*150
        visit[s]=True
        while(len(queue)>0):
            node=queue.pop(0)
            print(node,end="")
            for i in self.graph[node]:
                if(visit[i]==False):
                    queue.append(i)
                    visit[i]=True
g=Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(3,7)
goal=int(input("enter goal node:"))
res=g.BFS(1,goal)
if(res):
    print("goal state found")
else:
    print("goal state not found")
g.BFSTraversal(1)

