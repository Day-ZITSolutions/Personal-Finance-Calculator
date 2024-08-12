import os
import sys

# Set the working directory to the project root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_USER = os.getenv("DATABASE_USER", "root")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "")
DATABASE_PORT = os.getenv("DATABASE_PORT",3306)
DATABASE_NAME = os.getenv("DATABASE_NAME", "personal_finance")