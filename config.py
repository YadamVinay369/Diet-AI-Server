import os
import json
from dotenv import load_dotenv


class Config:
    MONGOURL: str
    SECRET_KEY: str
    API_KEYS: list[str]
    
    CLASSIFICATION_PROMPT: str
    CLASSIFICATION_SYSTEM_PROMPT: str
    
    OMNI_KNOWLEDGE_BOT_PROMPT: str
    OMNI_KNOWLEDGE_BOT_SYSTEM_PROMPT: str
    
    NUTRISCANNER_PROMPT: str
    NUTRISCANNER_SYSTEM_PROMPT: str
    
    DIET_BUILDER_PROMPT: str
    DIET_BUILDER_SYSTEM_PROMPT: str
    
    NUTRI_REFLECTOR_PROMPT: str
    NUTRI_REFLECTOR_SYSTEM_PROMPT: str 
    
    MISSY_MONITOR_PROMPT: str
    MISSY_MONITOR_SYSTEM_PROMPT: str
    
    NUTRIENTS_LIST: list[str]  
    NUTRIENT_SHEET_PER_FOOD_ITEM: dict
    BALANCED_DIET_SHEET: dict 



def load_config():
    env = os.getenv("ENV", "development")

    if env == "development":
        load_dotenv(".env.development")

    config = Config()

    for key, type_hint in Config.__annotations__.items():
        value = os.getenv(key)

        if value is None:
            raise ValueError(f"{key} not set in environment")

        # convert lists and dicts from JSON
        if type_hint in [list[str], dict]:
            value = json.loads(value)

        setattr(config, key, value)

    return config

settings = load_config()