import os
import logging
from logging import Formatter, FileHandler
from flask import Flask, request, jsonify
from ocr import process_image


_VERSION = 1  # API version
app = Flask(__name__)


@app.route('/hello', methods=["GET"])
def hello():
    return jsonify({"output": "hello world"})

@app.route('/v{}/ocr'.format(_VERSION), methods=["POST"])
def ocr():
    url = request.get_json()
    url= url["image_url"]
        
    output = process_image(url)
    return jsonify({"output": output})
    # try:
    #     url = request.get_json()
    #     url= url["image_url"]
        
    #     output = process_image(url)
    #     return jsonify({"output": output})
    #     # return jsonify({"output": url["image_url"]})
        
    # except:
    #     return jsonify(
    #         {"error": "Did you mean to send: {'image_url': 'some_jpeg_url'}"}
    #     )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)