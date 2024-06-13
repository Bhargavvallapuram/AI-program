from queue import PriorityQueue
n=int(input("enter no of verties in graph"))
graph=[[]for i in range(n)]
def Best_First_Search(src,goal,n):
    flag=0
    pathcost=0
    visited=[False]*n
    pq=PriorityQueue()
    pq.put((0,src))
    print("travelling path")
    while pq.empty()==False:
        node=pq.get()
        node_cost=node[0]
        u=node[1]
        if u==goal:
            print(u)
            flag=1
            break
        else:
            print(u,end="__")
            visited[u]=True
        for v,c in graph[u]:
                if visited[v]==False:
                    c=c+node_cost
                    pq.put((c,v))
    if flag==1:
        print("search successful")
    else:
        print("search failure")
def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))
addedge(0,1,2)
addedge(0,2,4)
addedge(1,3,6)
addedge(1,4,3)
addedge(2,5,2)
addedge(2,6,5)
addedge(3,7,1)
addedge(3,8,4)
addedge(4,9,5)
addedge(4,10,8)
addedge(5,11,6)
addedge(5,12,4)
addedge(6,13,3)
#addedge(6,14,2)
source=int(input("enter source vertices:"))
target=int(input("enter goal vertices"))
Best_First_Search(source,target,n)
