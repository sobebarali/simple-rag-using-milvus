from environs import Env
import os

# List of environment variables to remove
env_vars_to_remove = ["OPENAI_API_KEY", "MILVUS_URI", "COLLECTION_NAME", "MILVUS_USER", "MILVUS_PASSWORD"]

for var in env_vars_to_remove:
    os.environ.pop(var, None)  # Remove the variable if it exists


# Initialize the Env instance
env = Env()
env.read_env()  # Read .env file, defaults to the current directory

# Access environment variables
OPENAI_API_KEY = env.str("OPENAI_API_KEY")
MILVUS_URI = env.str("MILVUS_URI", "http://localhost:19530")
COLLECTION_NAME = env.str("COLLECTION_NAME", "test_collection")
MILVUS_USER = env.str("MILVUS_USER", "test_user")
MILVUS_PASSWORD = env.str("MILVUS_PASSWORD", "test_password")
MILVUS_TOKEN = env.str("MILVUS_TOKEN", "test_token")

# Print all variables
print(f"OPENAI_API_KEY: {OPENAI_API_KEY}")
print(f"MILVUS_URI: {MILVUS_URI}")
print(f"COLLECTION_NAME: {COLLECTION_NAME}")
print(f"MILVUS_USER: {MILVUS_USER}")
print(f"MILVUS_PASSWORD: {MILVUS_PASSWORD}")
print(f"MILVUS_TOKEN: {MILVUS_TOKEN}")
