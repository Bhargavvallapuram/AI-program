import math
def AlphaBeta(nodeIndex,depth,values,alpha,beta,maxTern):
    if(depth==maxDepth):
        return values[nodeIndex]
    if(maxTern):
        maxEva=-10000
        for k in range(2):
            eva=AlphaBeta(nodeIndex*2+k,depth+1,values,alpha,beta,False)
            maxEva=max(maxEva,eva)
            alpha=max(alpha,maxEva)
            if(alpha>=beta):
                print("pruned at right sub tree")
                print("alpha",alpha)
                print("beta",beta)
                break
        return maxEva
    else:
        minEva=+10000
        for k in range(2):
            eva=AlphaBeta(nodeIndex*2+k,depth+1,values,alpha,beta,True)
            minEva=min(minEva,eva)
            beta=min(beta,minEva)
            if(alpha>=beta):
                print("pruned at right sub tree")
                print("alpha",alpha)
                print("beta",beta)
                break
        return minEva
values=[1,2,3,4,5,6,7,8]
maxDepth=math.log(len(values),2)
print("optimal value",AlphaBeta(0,0,values,-10000,10000,True))