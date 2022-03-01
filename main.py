from fastapi import FastAPI
from routes.year_route import courses_api_router

app = FastAPI()

app.include_router(courses_api_router)
