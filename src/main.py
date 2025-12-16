import os
import redis
from dotenv import load_dotenv

load_dotenv()

class RedisConfig:
    def __init__(self):
        self.host = os.getenv('REDIS_HOST', 'localhost')
        self.port = int(os.getenv('REDIS_PORT', 6379))
        self.password = os.getenv('REDIS_PASSWORD', None)
        self.db = int(os.getenv('REDIS_DB', 0))
        self.connection = None

    def connect(self):
        try:
            self.connection = redis.Redis(
                host=self.host,
                port=self.port,
                password=self.password,
                db=self.db,
                decode_responses=True
            )
            self.connection.ping()
            print("Connected to Redis successfully.")
        except redis.ConnectionError as e:
            print(f"Failed to connect to Redis: {e}")

    def get_connection(self):
        if not self.connection:
            self.connect()
        return self.connection

if __name__ == "__main__":
    redis_config = RedisConfig()
    redis_conn = redis_config.get_connection()
    redis_conn.set("test_key", "test_value")
    print(redis_conn.get("test_key"))