from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    """This is an asynchronous function that functions as the root of the API

    Returns:
        JSON: Returns your typical JSON string although it is hardcoded
    """
    return {
        "message": "Hello World"
    }
