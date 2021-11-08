"""
Basic API that grabs dog name input, sub breed and returns a random image.
Also returns a list of all breeds available
Written for Knight Hacks Intro to Python Workshop 2021
Abrahan Nevarez
"""
from flask import Flask, request
import requests
import json
from flask_cors import CORS
from flasgger import Swagger
app = Flask(__name__, static_url_path="/static")
app.config['SWAGGER'] = {
    'title': 'Dog Fetching API',
    'uiversion': 3,
    'version': '0.1.1'
}
CORS(app)
swagger = Swagger(app)
@app.route("/get_dog_breeds/", methods=["GET"])
def get_dog_breeds():
    """
    Fetches all the dog breeds available
    ---
    responses:
        200:
            description: Dog breeds successfully retrieved
        401:
            description: Could not retrieve the dog list
    """
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    response_json = response.json()
    return response_json["message"]

@app.route("/get_dog_image/", methods=["GET"])
def get_dog_image():
    """
    Requires a dog name to be given
    Sub breed name is optional for the sub species
    Returns an json response
    ---
    parameters:
        - name: breed_name
          in: query
          type: string
          required: true
        - name: sub_breed_name
          in: query
          type: string
          required: false
    responses:
        200:
            description: dog image was fetched
        400:
            description: dog image could not be found
    """
    if request.method == "GET":
        breed_name = request.args.get("breed_name")
        if(request.args.get("sub_breed_name") is not None):
            sub_breed_name = request.args.get("sub_breed_name")
            response = requests.get(f"https://dog.ceo/api/breed/{breed_name}/{sub_breed_name}/images/random")
        else:
            response = requests.get(f"https://dog.ceo/api/breed/{breed_name}/images/random")
        return response.json()


if __name__ == "__main__":
    app.run(port=8080)