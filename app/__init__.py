import os
import redis
from dotenv import load_dotenv

load_dotenv()

db = redis.StrictRedis(
    host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), password=os.getenv('REDIS_PASSWORD'), decode_responses=True
)
