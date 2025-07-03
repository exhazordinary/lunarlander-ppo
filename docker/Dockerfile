FROM python:3.10-slim

# Install system dependencies for gym[box2d]
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    swig \
    python3-dev \
    libgl1-mesa-glx \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Create models directory for saving checkpoints
RUN mkdir -p models

# Default command
CMD ["python", "train.py"]

