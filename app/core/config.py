import os
from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRED_IN_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRED_IN_MINUTES"))
REFRESH_TOKEN_EXPIRED_IN_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRED_IN_DAYS"))