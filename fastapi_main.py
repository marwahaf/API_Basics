# First API using FastAPI
# Tuto 1 -with FastAPI: https://fastapi.tiangolo.com/tutorial/

from enum import Enum
from typing import Union

import pandas as pd
from fastapi import FastAPI
# Tuto 2 - with FastAPI : https://anderfernandez.com/en/blog/how-to-create-api-python/
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

# Define the API
app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# To check : You can choose model among the list in the swagger UI doc
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/")
def read_root(name="World"):
    return {"Hello": f"{name}"}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/get-iris")
def get_iris():

    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
    iris = pd.read_csv(url)

    return iris


# http://localhost:8000/get-iris


@app.get("/plot-iris")
def plot_iris():

    import matplotlib.pyplot as plt
    import pandas as pd

    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
    iris = pd.read_csv(url)

    plt.scatter(iris["sepal_length"], iris["sepal_width"])
    plt.savefig("iris.png")
    file = open("iris.png", mode="rb")
    return StreamingResponse(file, media_type="image/png")


# http://localhost:8000/plot-iris
