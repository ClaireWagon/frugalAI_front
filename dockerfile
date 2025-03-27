FROM python:3.10-slim

# Set environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # Poetry configuration
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set up working directory
WORKDIR /app

# Copy Poetry configuration files
COPY pyproject.toml ./
# Copy the rest of the application
COPY . .

# Install dependencies
RUN poetry install --only main

# Expose the port the app runs on
EXPOSE 8501

# Command to run the application
CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
