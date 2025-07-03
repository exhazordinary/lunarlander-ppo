import gymnasium as gym
from stable_baselines3 import PPO
import time

env = gym.make("LunarLander-v3", render_mode="human")
model = PPO.load("ppo_lunarlander")

for episode in range(3):
    obs, _ = env.reset()
    done = False
    total_reward = 0
    while not done:
        action, _ = model.predict(obs)
        obs, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        total_reward += reward
        time.sleep(0.02)
    print(f"Episode {episode+1}: Reward = {total_reward}")
env.close()
