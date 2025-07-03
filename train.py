import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.logger import configure

print("🚀 Starting PPO training...")

log_path = "./logs/"
new_logger = configure(log_path, ["stdout", "tensorboard"])

env = Monitor(gym.make("LunarLander-v3"))

model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=2.5e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    gae_lambda=0.95,
    clip_range=0.2,
    ent_coef=0.01,
    tensorboard_log=log_path,
)
model.set_logger(new_logger)

checkpoint_callback = CheckpointCallback(save_freq=10_000, save_path="./models", name_prefix="ppo_checkpoint")

model.learn(total_timesteps=100_000, callback=checkpoint_callback)
model.save("ppo_lunarlander")

env.close()
print("✅ Training complete and model saved.")
