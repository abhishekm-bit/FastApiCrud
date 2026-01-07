from fastapi import FastAPI
from Crud_FastApi.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (for local dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

@app.get("/")

def root():
    return {"status": "API running"}
