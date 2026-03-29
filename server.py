from fastapi import FastAPI
from routes.routes import router
from routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    # "http://localhost:5173",
    # "http://127.0.0.1:5173",
    "https://get-healthy-with-diet-ai.netlify.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.include_router(auth_router)

@app.get('/')
def home():
    
    '''
    after logging in , 
    1. we fetch overall_nutrient_intake_sheet
    2. Check missing dates and call missy monitor if required
    '''
    print("Welcome to Home...!")
    return {"message":"Home called!" }

