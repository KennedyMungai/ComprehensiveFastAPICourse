"""
The main File for this API project
Author: Kennedy Mungai
Project: ComprehensiveFastAPICourse
    I'm currently taking a FastAPI course from freecodecamp
"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    """This is an asynchronous function that functions as the root of the API

    Returns:
        JSON: Returns your typical JSON string although it is hardcoded
    """
    return {
        "message": "Welcome to this dank API"
    }
