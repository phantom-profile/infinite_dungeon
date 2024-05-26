from pathlib import Path

import django
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / '.env'

load_dotenv(ENV_FILE)
django.setup()
