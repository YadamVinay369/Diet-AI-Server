from motor.motor_asyncio import AsyncIOMotorClient
from config import load_config
config = load_config()

client = AsyncIOMotorClient(config.MONGOURL)
db=client["dietvite"]
