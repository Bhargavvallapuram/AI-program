from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self,start,goal):
        if(start==goal):
            return True
        for node in self.graph[start]:
            if(self.DFS(node,goal)):
                return True
        return False
    def DFSTraversal(self,v):
        visit=set()
        self.printDFS(v,goal,visit)
    def printDFS(self,v,goal,visit):
            if(v==goal):
                print(goal)
                return True
            else:
                visit.add(v)
                print(v,end="")
                for cnode in self.graph[v]:
                    if cnode not in visit and v!=goal:
                        self.printDFS(cnode,goal,visit)
                return False
g=Graph()
g.addEdge('X','Y')
g.addEdge('X','Z')
g.addEdge('Y','A')
g.addEdge('Y','B')
g.addEdge('Z','C')
g.addEdge('Z','D')
g.addEdge('A','E')
g.addEdge('B','F')
g.addEdge('B','G')
g.addEdge('D','H')
g.addEdge('D','I')

goal=input("enter goal node")
res=g.DFS('A',goal)
if(res):
    print("goal state found")
else:
    print("goal is not found")
g.DFSTraversal('A')

