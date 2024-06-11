import gymnasium as gym



# LunarLander
def game1():
    env = gym.make("LunarLander-v2", render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()

def game2():
    env = gym.make("FrozenLake-v1", render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()


def game3():
    env = gym.make("Acrobot-v1", render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()
    
def game4():
    env = gym.make("Humanoid-v4", render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()

def game5():
    env = gym.make("ALE/Asteroids-v5", render_mode="human")
    observation, info = env.reset()

    for _ in range(1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()

# Stan gry i zestaw akcji dyskretne:
#   Frozen Lake
# game2()
    
# Stan gry jest ciągły (nieskończony, liczby zmiennoprzecinkowe), ale zestaw akcji jest dyskretny
#   Lunar Lander
# game1()
    
# Stan gry i zestaw akcji jest ciągły.
# Humanoid
# game4()
    
def podpunkt_d():
    env = gym.make("FrozenLake-v1", render_mode="human", is_slippery=False)
    observation, info = env.reset()

    win_actions = [2, 2, 1, 1, 1, 1, 2]
    for action in win_actions:
        observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()
    for i in range(10, 1000):
        action = env.action_space.sample()  # agent policy that uses the observation and info

        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
podpunkt_d()