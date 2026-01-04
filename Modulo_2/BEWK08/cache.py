import redis
import json

class CacheManager:
    def __init__(self, host, port, password, *args, **kwargs):
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            password=password,
            *args,
            **kwargs
        )
        connection_status = self.redis_client.ping()
        if connection_status:
            print('Connection created succesfully')
    
    # Functions to store data on cache
    def store_data(self, key, value, time_to_live=None):
        try:
            if time_to_live is None:
                self.redis_client.set(key, value)
            else:
                self.redis_client.setex(key, time_to_live, value)
        except redis.RedisError as error:
            print(f"An error ocurred while storing data in Redis: {error}")

    # Function to check if data is stored on cache
    def check_key(self, key):
        try:
            key_exists = self.redis_client.exists(key)
            if key_exists:
                ttl = self.redis_client.ttl(key)
                return True, ttl

            return False, None
        except redis.RedisError as error:
            print(f"An error ocurred while checking a key in Redis: {error}")
            return False, None

    # Function to retrieve data from cache
    def get_data(self, key):
        try:
            output = self.redis_client.get(key)
            if output is not None:
                result = output.decode("utf-8")
                return result
            else:
                return None
        except redis.RedisError as error:
            print(f"An error ocurred while retrieving data from Redis: {error}")

    # Function to delete data from cache
    def delete_data(self, key):
        try:
            output = self.redis_client.delete(key)
            return output == 1
        except redis.RedisError as error:
            print(f"An error ocurred while deleting data from Redis: {error}")
            return False

    # Function to delete data with pattern, useful for bulk delete 
    def delete_data_with_pattern(self, pattern):
        try:
            # Iterar sobre las claves que coinciden con el patrón
            for key in self.redis_client.scan_iter(match=pattern):
                self.delete_data(key)
        except redis.RedisError as error:
            print(f"An error ocurred while deleting data from Redis: {error}")
    
    def store_json(self, key, data, time_to_live=None):
        try:
            json_str = json.dumps(data)
            self.store_data(key, json_str, time_to_live)
        except (TypeError, redis.RedisError) as error:
            print(f"Error storing JSON in cache: {error}")
    
    def get_json(self, key):
        try:
            data = self.redis_client.get(key)
            if data:
                return json.loads(data)
            return None
        except (redis.RedisError, json.JSONDecodeError) as error:
            print(f"Error getting JSON from cache: {error}")
            return None


cache_manager = CacheManager(
    host="PLACEHOLDER",
    port=19813,
    password='PLACEHOLDER'
)

