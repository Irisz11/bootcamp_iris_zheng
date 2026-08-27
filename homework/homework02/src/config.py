import os
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    """Load environment variables from the project's .env file."""
    env_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(env_path)


def get_key(name: str, default=None):
    """Return an environment variable or a default value."""
    return os.getenv(name, default)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"