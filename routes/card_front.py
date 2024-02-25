import cv2
import numpy as np
from flask import Blueprint, request, jsonify

from utilities.ExtractFrontText import extract_front_information

card_front_blueprint = Blueprint('card_front', __name__)


@card_front_blueprint.route('/card_front', methods=['POST'])
def extract_front_information_route():

    if 'image' not in request.files:
        return jsonify({'error': 'No image provided for the front of the card'}), 400

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({'error': 'Empty image file provided for the front of the card'}), 400

    image_array = np.frombuffer(image_file.read(), np.uint8)

    # Decode image
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Extract information from the front of the card
    extracted_info = extract_front_information(image)
    return jsonify(extracted_info)
