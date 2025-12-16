# __init__.py

from .config import load_config
from .ingestion import loader

config = load_config()

__all__ = ["config", "loader"]
