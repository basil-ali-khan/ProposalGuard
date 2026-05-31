import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.apis.proposal import router as proposal_router

app = FastAPI(title="ProposalGuard API")

_raw_origins = os.environ.get("ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
_allowed_origins = [o.strip() for o in _raw_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(proposal_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to ProposalGuard API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}