"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# API Provider: "openrouter" or "openai"
API_PROVIDER = os.getenv("API_PROVIDER", "openrouter")

# OpenRouter API key (if using OpenRouter)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenAI API key (if using OpenAI directly)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Council members - model identifiers
if API_PROVIDER == "openai":
    # OpenAI models
    COUNCIL_MODELS = [
        "gpt-4o",
        "gpt-4o-mini", 
        "gpt-4-turbo",
        "gpt-3.5-turbo",
    ]
    CHAIRMAN_MODEL = "gpt-4o"
    API_URL = "https://api.openai.com/v1/chat/completions"
    API_KEY = OPENAI_API_KEY
else:
    # OpenRouter models (default)
    COUNCIL_MODELS = [
        "openai/gpt-4o",
        "google/gemini-2.0-flash-001",
        "anthropic/claude-3.5-sonnet",
        "meta-llama/llama-3.1-70b-instruct",
    ]
    CHAIRMAN_MODEL = "google/gemini-2.0-flash-001"
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    API_KEY = OPENROUTER_API_KEY

# Data directory for conversation storage
# On Heroku, use /tmp which is ephemeral but writable
# For persistent storage, consider using a database or S3
DATA_DIR = os.getenv("DATA_DIR", "data/conversations")
