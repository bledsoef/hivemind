from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware  # Import the CORS middleware
import api.controllers.tmyk as tmyk
from mangum import Mangum
import uvicorn
from database.config import engine, SessionLocal, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow both POST and OPTIONS methods
    allow_headers=["*"],
)

app.include_router(tmyk.router)
# app.include_router(user.router)
# app.include_router(classes.router)

Base.metadata.create_all(bind=engine)
handler = Mangum(app)

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)