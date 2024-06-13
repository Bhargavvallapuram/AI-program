import math
def MiniMax(nodeIndex,depth,values,maxTern):
    if(depth==maxDepth):
        return values[nodeIndex]
    if(maxTern):
        maxEva=-10000
        for k in range(2):
            eva=MiniMax(nodeIndex*2+k,depth+1,values,False)
            maxEva=max(maxEva,eva)
        return maxEva
    else:
        minEva=+10000
        for k in range(2):
            eva=MiniMax(nodeIndex*2+k,depth+1,values,True)
            minEva=min(minEva,eva)
        return minEva
values=[4,-1,8,5,-7,-4,-2,-1]
maxDepth=math.log(len(values),2)
print("optimal value",MiniMax(0,0,values,True))