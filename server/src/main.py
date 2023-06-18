from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from model import Base
from controller.auth_controller import router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)


app.include_router(router, prefix="/api/v1/auth ", tags=["auth"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5000)
