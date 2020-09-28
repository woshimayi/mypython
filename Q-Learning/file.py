import gym
import numpy as np


env = gym.make('FrozenLake-v0')

# Implement Q-Table learning algorithm
# 实现Q表学习算法
# Initialize table with all zeros
# 初始化Q表为全0值
Q = np.zeros([env.observation_space.n, env.action_space.n])
# Set learning parameters
# 设置学习参数
lr = .8
y = .95
num_episodes = 2000
# create lists to contain total rewards and steps per episode
# 创建列表以包含每个episode的总回报与总步数
#jList = []
rList = []
for i in range(num_episodes):
    # Reset environment and get first new observation
    # 初始化环境并获得第一个观察
    s = env.reset()
    rAll = 0
    d = False
    j = 0
    # The Q-Table learning algorithm
    # Q表学习算法
    while j < 99:
        j += 1
        # Choose an action by greedily (with noise) picking from Q table
        # 基于Q表贪婪地选择一个最优行动（有噪音干扰）
        a = np.argmax(Q[s, :] + np.random.randn(1,
                                                env.action_space.n) * (1. / (i + 1)))
        # Get new state and reward from environment
        # 从环境中获得回报和新的状态信息
        s1, r, d, _ = env.step(a)

        # Update Q-Table with new knowledge
        # 用新的知识更新Q表
        Q[s, a] = Q[s, a] + lr * (r + y * np.max(Q[s1, :]) - Q[s, a])
        rAll += r
        s = s1
        if d:
            break
    # jList.append(j)
    rList.append(rAll)

print("Score over time: " + str(sum(rList) / num_episodes))

print("Final Q-Table Values")
print(Q)
