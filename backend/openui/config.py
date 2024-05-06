import os
from pathlib import Path
import secrets
from urllib.parse import urlparse
from enum import Enum


class Env(Enum):
    LOCAL = 1
    PROD = 2
    DEV = 3


try:
    env = os.getenv("OPENUI_ENVIRONMENT", "local")
    if env == "production":
        env = "prod"
    elif env == "development":
        env = "dev"
    ENV = Env[env.upper()]
except KeyError:
    print("Invalid environment, defaulting to running locally")
    ENV = Env.LOCAL

default_db = Path.home() / ".openui" / "db.sqlite"
default_db.parent.mkdir(exist_ok=True)
DB = os.getenv("DATABASE", default_db)
HOST = os.getenv(
    "OPENUI_HOST",
    "https://localhost:5173" if ENV == Env.DEV else "http://localhost:7878",
)
RP_ID = urlparse(HOST).hostname
SESSION_KEY = os.getenv("OPENUI_SESSION_KEY")
if SESSION_KEY is None:
    env_path = Path.home() / ".openui" / ".env"
    if env_path.exists():
        SESSION_KEY = env_path.read_text().splitlines()[0].split("=")[1]
    else:
        SESSION_KEY = secrets.token_hex(32)
        with env_path.open("w") as f:
            f.write("OPENUI_SESSION_KEY={SESSION_KEY}")
# GPT 3.5 is 0.0005 per 1k tokens input and 0.0015 output
# 700k puts us at a max of $1.00 spent per user over a 48 hour period
MAX_TOKENS = int(os.getenv("OPENUI_MAX_TOKENS", "700000"))
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

AWS_ENDPOINT_URL_S3 = os.getenv("AWS_ENDPOINT_URL_S3")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME", "openui")
