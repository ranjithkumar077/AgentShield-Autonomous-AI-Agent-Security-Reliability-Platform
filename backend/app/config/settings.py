# settings.py
"""Application settings loaded from environment variables.

We use `python-dotenv` so developers can place a `.env` file locally. In production the
environment will provide the variables (e.g., `GEMINI_API_KEY`).
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env if present at project root
BASE_DIR = Path(__file__).resolve().parents[3]
DOTENV_PATH = BASE_DIR / ".env"
if DOTENV_PATH.exists():
    load_dotenv(dotenv_path=DOTENV_PATH)

# Settings
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

# Model selection – default to Gemini free tier
DEFAULT_MODEL = "gemini-1.5-flash"  # free‑tier Gemini model identifier
