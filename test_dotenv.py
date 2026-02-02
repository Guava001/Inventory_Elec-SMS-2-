from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file in the same folder

print("TEST_ENV =", os.getenv("TEST_ENV"))
