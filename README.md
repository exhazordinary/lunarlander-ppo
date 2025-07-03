# LunarLander Minimal Agent

A minimal implementation for running the OpenAI Gym LunarLander-v3 environment using random actions. This project provides simple scripts to interact with the environment and observe agent performance.

## Features

- Run LunarLander-v3 (Box2D) with a random agent
- Simple training and evaluation scripts
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
└── .gitignore
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

### Run Training Script

```
python train.py
```

- Runs a random agent on LunarLander-v3 for several episodes.
- Prints the reward for each episode and the average reward.

### Run Evaluation Script

```
python evaluate.py
```

- Runs a random agent on LunarLander-v3 for several episodes.
- Renders the environment and prints the reward for each episode and the average reward.

## References

- [OpenAI Gymnasium](https://gym.openai.com/)

## License

MIT License
