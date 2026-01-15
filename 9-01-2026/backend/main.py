from fastapi import FastAPI
from api.syllabus import router
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()

app.include_router(router,prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"msg":"EdTech AI Backend Running"}
