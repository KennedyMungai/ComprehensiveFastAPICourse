"""
    The main File for this API project
    Author: Kennedy Mungai
    Project: ComprehensiveFastAPICourse
        I'm currently taking a FastAPI course from freecodecamp
"""
from typing import Optional
from random import randrange
from fastapi import FastAPI, Response, status, HTTPException
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


my_posts = [
    {"title": "title of post 1", "content": "Content of post 1", "id": 1},
    {"title": "Favorite foods", "content": "I like pizza", "id": 2},
]


def find_post(_id: int):
    """
    This is a function whose work is to find the posts

    Args:
        id (int): This is the Id of the post
    """
    for _p in my_posts:
        if _p["id"] == _id:
            return _p


@app.get("/")
def root():
    """
        This is an asynchronous function that functions as the root of the API

        Returns:
            JSON: Returns your typical JSON string although it is hardcoded
    """
    return {"data": my_posts}


@app.get("/posts")
def get_posts():
    """
        This is a simple function that retrieves all the posts
    """
    return {"data": " This is all your posts"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    """
        This is an API function thar creates posts
    """
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)

    my_posts.append(post_dict)

    return {"data": f"{post_dict}"}


@app.get("/posts/{post_id}")
def get_post(post_id: int, response: Response):
    """
        This function is meant to fetch one individual post
    Args:
        id (int): The id of the post is passed here
    """
    post = find_post(post_id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return {"Post": post}


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    """A simple function for deleting posts

    Args:
        post_id (int): The id of the post to be deleted
    """
