import re
from datetime import datetime

import pytesseract
from PIL import Image
from flask import Blueprint, jsonify, request

card_back_blueprint = Blueprint('card_back', __name__)


@card_back_blueprint.route('/card_back', methods=['POST'])
def process_id_card():
    image_file = request.files['image']

    image = Image.open(image_file)

    ocr_text = pytesseract.image_to_string(image)

    date_pattern = r'\b(?:\d{1,2}[./-]\d{1,2}[./-]\d{2,4}|\d{4}[./-]\d{1,2}[./-]\d{1,2})\b'

    date_matches = re.findall(date_pattern, ocr_text)

    issuing_date = None
    expiry_date = None

    if len(date_matches) >= 2:
        issuing_date = date_matches[0]
        expiry_date = date_matches[1]

    is_expired = False

    if expiry_date:
        expiry_datetime = datetime.strptime(expiry_date, '%Y/%m/%d')
        current_datetime = datetime.now()

        if expiry_datetime < current_datetime:
            is_expired = True

    response_data = {
        "issuing_date": issuing_date,
        "expiry_date": expiry_date,
        "is_expired": is_expired
    }

    return jsonify(response_data)
