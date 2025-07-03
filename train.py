import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor

print("🚀 Starting PPO training...")

env = Monitor(gym.make("LunarLander-v3"))
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100_000)
model.save("ppo_lunarlander")

env.close()
print("✅ Training complete and model saved.")
