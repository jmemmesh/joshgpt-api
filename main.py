from fastapi import FastAPI
import uvicorn
from api import api_router
from lifespan.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)