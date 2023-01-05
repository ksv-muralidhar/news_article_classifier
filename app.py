from flask import Flask, render_template, request
import requests
import numpy as np
from utils.get_api_url import get_api_url
from flask_cors import cross_origin, CORS
from logger.logger import MongoLogger


app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)
API = get_api_url()  # get the URL of API. if no env var is present it defaults to localhost


@app.route("/")
@cross_origin()
def index():
    """
    displays the index.html page
    """
    logger = MongoLogger()
    logger.log_to_db(level="INFO", message="entering index.html")
    return render_template("index.html")


@app.route("/", methods=["POST"])
@cross_origin()
def form_prediction():
    """
    Returns the API response based on the inputs filled in the form.
    """
    logger = MongoLogger()
    try:
        logger.log_to_db(level="INFO", message="clicked predict in index.html (form prediction)")
        logger.log_to_db(level="INFO", message="entering form_prediction")
        # assigning the inputs from the form to respective variables.
        text = request.form["text_input"]
        # input json to the API in the required format
        request_json = {"text": text}

        error = ""
        response = requests.post(url=API, json=request_json)
        if response.status_code == 200:
            response_json = response.json()
            predicted_label = response_json.get("result")
            confidence_level = response_json.get("confidence")
            response = [f'{p} ({c}%)' for p, c in zip(predicted_label, confidence_level)]
            result = f'<p>Top 2 Tags:</p> <p>{", ".join(response)}</p>'
        else:
            result = f'Error: Details at the bottom'
            error = response.json()
            logger.log_to_db(level="CRITICAL", message=error)
    except Exception as e:
        result = f'Error: Details at the bottom'
        error = e
        logger.log_to_db(level="CRITICAL", message=str(error))
    logger.log_to_db(level="INFO", message="exiting form_prediction")
    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
