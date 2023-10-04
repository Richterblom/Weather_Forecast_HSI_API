from fastapi import FastAPI, HTTPException
from api import api_info

app = FastAPI()


@app.get('/')
async def root():
    return {'example': 'this is an example', 'data': 0}

"""
Created an If statement that checked if the latitude and longitude where in the given range it would raise and exception
Could use float due to me using .format in api.py.
Not 100% sure how fastapi does error handling for url's could not get it to throw an exception when user enters text for
lat and long in url but /docs it was a required field.
"""


@app.get('/weather')
# I saw you could you ge and le for greater than and less than but it bugged my code out with 422 Unprocessable Entity
async def get_root(latitude: float, longitude: float):
    if -90 < latitude < 90 and -180 < longitude < 180:
        return api_info(latitude, longitude)
    else:
        raise HTTPException(status_code=400, detail="Your latitude and longitude are not in the specified range")

# GET /weather?latitude=12.34&longitude=56.78




