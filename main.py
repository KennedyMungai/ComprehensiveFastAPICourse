"""
    The main File for this API project
    Author: Kennedy Mungai
    Project: ComprehensiveFastAPICourse
        I'm currently taking a FastAPI course from freecodecamp
"""
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    """
        This is an asynchronous function that functions as the root of the API

        Returns:
            JSON: Returns your typical JSON string although it is hardcoded
    """
    return {
        "message": "Welcome to this dank API"
    }


@app.get("/posts")
def get_posts():
    """
        This is a simple function that retrieves all the posts
    """
    return {"data": " This is all your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    """
        This is an API function thar creates posts
    """

    print(payload)

    return {"new_post": f"Title:- {payload['title']} Content:- {payload['content']}"}
