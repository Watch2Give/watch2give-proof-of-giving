from fastapi import FastAPI
from proof_of_giving.router import router as proof_router

app = FastAPI()
app.include_router(proof_router)
