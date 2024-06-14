import numpy as np
SMALL_ENOUGH = 0.005
GAMMA = 1
NOISE = 0.1
all_states=[]
for i in range(3):
    for j in range(4):
            all_states.append((i,j))
rewards = {}
for i in all_states:
    if i == (2,3):
        rewards[i] = +1
    elif i == (1,3):
        rewards[i] = -1
    elif i == (1,1):
        rewards[i] = 0
    else:
        rewards[i] = -0.04
actions = {
    (0,0):('D', 'R'),
    (0,1):('R', 'L'),
    (0,2):('D', 'L', 'R'),
    (0,3):('D', 'L'),
    (1,0):('D', 'U'),
    (1,2):('D', 'U', 'R'),
    (2,0):('U', 'R'),
    (2,1):('L', 'R'),
    (2,2):('L', 'R', 'U')    
    }
policy={}
for s in actions.keys():
    policy[s] = np.random.choice(actions[s])
V={}
for s in all_states:
    if s in actions.keys():
        V[s] = -0.04
    if s ==(2,3):
        V[s]=+1
    if s == (1,3):
        V[s]=-1
    if s == (1,1):
        V[s]=0
iteration = 0
while True:
    biggest_change = 0
    for s in all_states:
        if s in policy:

            old_v = V[s]
            new_v = 0

            for a in actions[s]:
                if a == 'U':
                    nxt = [s[0]-1, s[1]]
                if a == 'D':
                    nxt = [s[0]+1, s[1]]
                if a == 'L':
                    nxt = [s[0], s[1]-1]
                if a == 'R':
                    nxt = [s[0], s[1]+1]

                
                    
                random_1 = np.random.choice([i for i in actions[s] if i != a])
                if random_1 == 'U':
                    act = [s[0]-1, s[1]]
                if random_1 == 'D':
                    act = [s[0]+1, s[1]]
                if random_1 == 'L':
                    act = [s[0], s[1]-1]
                if random_1 == 'R':
                    act = [s[0], s[1]+1]
                nxt = tuple(nxt)
                act = tuple(act)
                v = rewards[s] + (GAMMA * ((1-NOISE)* V[nxt] + (NOISE * V[act])))
                if v > new_v:
                    new_v = v
                    policy[s] = a
            V[s] = new_v
            if np.abs(V[s] - old_v) > biggest_change:
                biggest_change = np.abs(V[s] - old_v) 
    if biggest_change < SMALL_ENOUGH:
        break
    iteration += 1

print("Utility values for each block : ")
for key, value in V.items():
    print(key, ' : ', value)

print("Number of iterations : ",iteration)