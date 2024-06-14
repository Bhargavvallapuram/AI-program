actions = (0, 1)
states=[]
for i in range(3):
    for j in range(4):
            states.append((i,j))
rewards = {}
for i in states:
    if i == (2,3):
        rewards[i] = +1
    elif i == (1,3):
        rewards[i] = -1
    elif i == (1,1):
        rewards[i] = 0
    else:
        rewards[i] = -0.04
gamma = 0.1
delta=5 
probs = [
    [[0.1, 0.9], [0.9, 0.1], [0.1, 0.9], [0.1, 0.9]],
    [[0.1, 0.9], [0, 0], [0.9, 0.1], [0, 0]],
    [[0.9, 0.1], [0.9, 0.1], [0.1, 0.9], [0, 0]]
]
max_policy_iter = 10000    
max_value_iter = 10000
pi = [0 for s in states]
V = [0 for s in states]
for i in range(max_policy_iter):
    optimal_policy_found = True
    for j in range(max_value_iter):
        max_diff = 0
        V_new = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for s in states:
            val = rewards[s]
            for s_next in states:
                val += probs[s[0]][s_next[1]][pi[s[0]]] * (gamma * V[s_next[1]])
            max_diff = max(max_diff, abs(val - V[s[0]]))
            V[s[0]] = val
        if max_diff < delta:
            break      
    for s in states:
        val_max = V[s[0]]
        for a in actions:
            val = rewards[s] 
            for s_next in states:
                val += probs[s[0]][s_next[1]][a] * (gamma * V[s_next[1]])           
            if val > val_max and pi[s[0]] != a:
                pi[s[0]] = a
                val_max = val
                optimal_policy_found = False
    if optimal_policy_found:
        break
print("Policy Values")
print(pi)
print("Number of iterations : ")
print(i)
