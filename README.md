# LunarLander PPO Agent

A minimal implementation for training and evaluating a Proximal Policy Optimization (PPO) agent on the OpenAI Gymnasium LunarLander-v3 environment using [stable-baselines3](https://stable-baselines3.readthedocs.io/). This project provides scripts to train a PPO agent, save checkpoints, log to TensorBoard, and evaluate the trained model with rendering.

## Features

- Train a PPO agent on LunarLander-v3 (Box2D) using stable-baselines3
- Save model checkpoints and final trained model
- TensorBoard logging for training metrics
- Evaluate the trained agent with environment rendering
- Easy setup with pip or Docker

## File Structure

```
lunarlander-ppo/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── train.py
├── evaluate.py
├── README.md
├── .gitignore
├── models/
└── logs/
```

## Installation

### Manual

1. Install Python 3.8+ and pip.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Docker

1. Build the Docker image:
   ```
   docker-compose build
   ```
2. Run training:
   ```
   docker-compose run --rm app python train.py
   ```
3. Run evaluation:
   ```
   docker-compose run --rm app python evaluate.py
   ```

## Usage

### Train the PPO Agent

```
python train.py
```

- Trains a PPO agent on the LunarLander-v3 environment.
- Saves model checkpoints to the `models/` directory every 10,000 steps.
- Logs training metrics to the `logs/` directory for TensorBoard visualization.
- Saves the final trained model as `ppo_lunarlander`.

To view training progress in TensorBoard:
```
tensorboard --logdir logs/
```

### Evaluate the Trained Agent

```
python evaluate.py
```

- Loads the trained PPO model from `ppo_lunarlander`.
- Runs 3 evaluation episodes with environment rendering enabled.
- Prints the reward for each episode.

## Model Saving and Logs

- **Checkpoints:** Saved in the `models/` directory during training.
- **Final Model:** Saved as `ppo_lunarlander` in the project root.
- **Logs:** Training logs for TensorBoard are saved in the `logs/` directory.

## References

- [OpenAI Gymnasium](https://gymnasium.farama.org/)
- [Stable Baselines3](https://stable-baselines3.readthedocs.io/)

## License

MIT License
