"""
    The main File for this API project
    Author: Kennedy Mungai
    Project: ComprehensiveFastAPICourse
        I'm currently taking a FastAPI course from freecodecamp
"""
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    """
        This is a class that defined the type of data that is passed on to the CreatePosts function
    Args:
        BaseModel (_pydantic class_): I really dont know much about BaseModel
    """
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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
def create_posts(post: Post):
    """
        This is an API function thar creates posts
    """

    print(post)
    print(post.dict())

    return {"data": f"{post}"}
