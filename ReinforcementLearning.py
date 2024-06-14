import numpy as np

ROWS = 3
COLS = 4
WIN_STATE = (2, 3)
LOSE_STATE = (1, 3)
START = (0, 0)


class World:
    def __init__(self, state=START):
        self.state = state
        self.isEnd = False

    def giveReward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        elif self.state == (1, 1):
            return 0
        else:
            return -0.04

    def isEndFunc(self):
        if self.state == WIN_STATE or self.state == LOSE_STATE:
            self.isEnd = True

    def nextPosition(self, action):
        if action == "UP":
            nextState = (self.state[0] - 1, self.state[1])
        elif action == "DOWN":
            nextState = (self.state[0] + 1, self.state[1])
        elif action == "LEFT":
            nextState = (self.state[0], self.state[1] - 1)
        elif action == "RIGHT":
            nextState = (self.state[0], self.state[1] + 1)

        if 0 <= nextState[0] < ROWS and 0 <= nextState[1] < COLS and nextState != (1, 1):
            return nextState
        return self.state


class Agent:
    def __init__(self):
        self.states = []
        self.actions = ["UP", "DOWN", "LEFT", "RIGHT"]
        self.World = World()
        self.lr = 0.2
        self.exp_rate = 0.3
        self.state_values = {}
        for i in range(ROWS):
            for j in range(COLS):
                self.state_values[(i, j)] = 0

    def chooseAction(self):
        max_next_reward = 0
        action = ""
        if np.random.uniform(0, 1) <= self.exp_rate:
            action = np.random.choice(self.actions)
        else:
            for a in self.actions:
                next_reward = self.state_values[self.World.nextPosition(a)]
                if next_reward >= max_next_reward:
                    action = a
                    max_next_reward = next_reward
        return action

    def takeAction(self, action):
        self.World.state = self.World.nextPosition(action)

    def reset(self):
        self.states = []
        self.World = World()

    def play(self, rounds):
        i = 0
        while i < rounds:
            if self.World.isEnd:
                reward = self.World.giveReward()
                self.state_values[self.World.state] = reward
                print("Game End Reward:", reward)
                for s in reversed(self.states):
                    reward = self.state_values[s] + self.lr * (reward - self.state_values[s])
                    self.state_values[s] = round(reward, 3)
                self.reset()
                print("Iteration:", i, "Completed")
                print("______________________")
                i += 1
            else:
                action = self.chooseAction()
                self.states.append(self.World.state)
                print("Current State:", self.World.state, end="")
                print(" Actions:", action, end="")
                self.takeAction(action)
                self.World.isEndFunc()
                print(" Next state:", self.World.state)


if __name__ == "__main__":
    ag = Agent()
    ag.play(3)
    print("Utility values for each block:")
    for key, value in ag.state_values.items():
        print(key, ":", value)