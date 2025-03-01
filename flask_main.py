# Tuto used with Flask: https://anderfernandez.com/en/blog/how-to-create-api-python/
# Documentation with Flask: https://flask.palletsprojects.com/en/3.0.x/api/

import subprocess

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():

    name = request.args.get("name")

    if name is None:
        text = "Hello!"

    else:
        text = "Hello " + name + "!"

    return text


@app.route("/date", methods=["GET"])
def get_date():
    result = subprocess.check_output(["date"]).decode("utf-8")
    return jsonify({"date": result.strip()})


@app.route("/cal", methods=["GET"])
def get_cal():
    result = subprocess.check_output(["cal"]).decode("utf-8")
    return jsonify({"calendar": result.strip()})


@app.route("/docker", methods=["GET"])
def get_docker():
    result = subprocess.check_output(["docker", "ps"]).decode("utf-8")
    return jsonify({"docker": result.strip()})


@app.route("/cls", methods=["GET"])
def get_cls():
    result = subprocess.check_output(["cls"]).decode("utf-8")
    return jsonify({"cls": result.strip()})


@app.route("/get-iris")
def get_iris():

    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
    iris = pd.read_csv(url)

    return jsonify({"message": "Iris Dataset", "data": iris.to_dict()})


@app.route("/plot-iris")
def plot_iris():

    url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
    iris = pd.read_csv(url)

    # Save the plot in the directory
    plt.scatter(iris["sepal_length"], iris["sepal_width"])
    plt.savefig("iris.png")

    # Return the image file
    return send_file("iris.png")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
