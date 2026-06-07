from dotenv import load_dotenv
import os

load_dotenv()

app_name=os.getenv("APP_NAME")

print(f"{app_name} Backend started")