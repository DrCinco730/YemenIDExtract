import cv2
import pytesseract

from utilities.ExtractData import extract_formatted_data


def preprocess_image_for_ocr(image, use_denoised=True):
    """
    Preprocesses the image to improve OCR results.
    Parameters:
    - image: The input image.
    - use_denoised: A boolean indicating whether to use denoising in preprocessing.
    Returns:
    - Preprocessed image ready for OCR.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if use_denoised:
        processed_image = cv2.fastNlMeansDenoising(gray_image, None, 10, 7, 21)
    else:
        processed_image = gray_image
    th, threshed_image = cv2.threshold(processed_image, 127, 255, cv2.THRESH_TRUNC)
    return threshed_image


def extract_text_from_image(image):
    """
    Extracts concatenated text from the original and denoised images.
    Parameters:
    - image: The input image.
    Returns:
    - Concatenated extracted text from both preprocessing methods.
    """
    denoised_image = preprocess_image_for_ocr(image, use_denoised=True)
    original_threshed_image = preprocess_image_for_ocr(image, use_denoised=False)

    extracted_text_denoised = pytesseract.image_to_string(denoised_image, lang="ara+eng")
    extracted_text_original = pytesseract.image_to_string(original_threshed_image, lang="ara+eng")

    return extracted_text_denoised + extracted_text_original


def extract_front_information(image):
    extracted_text = extract_text_from_image(image)
    return extract_formatted_data(extracted_text)
