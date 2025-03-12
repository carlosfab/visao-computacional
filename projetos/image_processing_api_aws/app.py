from io import BytesIO
import numpy as np
import requests
from typing import Optional
import cv2
from PIL import Image


def deskew_image_api(img: np.ndarray, api_endpoint: Optional[str]) -> np.ndarray:
    """
    Send a request to the API to deskew the image.

    Args:
    - img (np.ndarray): The image to be deskewed, represented as a NumPy array.
    - api_endpoint (Optional[str]): The endpoint of the API that performs the deskewing.

    Returns:
    - np.ndarray: The deskewed image, represented as a NumPy array.

    Raises:
    - ValueError: If the API endpoint is None or if the API response is not successful.
    - requests.RequestException: If there is an issue with the network request.
    """
    if api_endpoint is None:
        raise ValueError("API endpoint is not specified.")

    try:
        # Encode the image to PNG format in memory
        result, img_buf = cv2.imencode('.png', img)
        if not result:
            raise ValueError("Image encoding failed.")

        img_bytes = img_buf.tobytes()

        # Send the encoded image to the API endpoint
        response = requests.post(url=api_endpoint, data=img_bytes)

        # Check if the request was successful
        if response.status_code == 200:
            # Open the image from the response content
            img_deskewed = Image.open(BytesIO(response.content))
            return np.asarray(img_deskewed)
        else:
            raise ValueError(f"API request failed with status code {response.status_code}")

    except requests.RequestException as e:
        raise requests.RequestException(f"Request failed: {e}")
    


# Para testar sem a API (local)
def deskew_image_api(img: np.ndarray) -> np.ndarray:
    """
    Simulate sending a request to an API to deskew the image.
    Instead of sending a network request, we directly call the local deskew function.
    """
    # Simulate the deskewing as if it were done by a remote API
    deskewed_img = deskew_image(img)

    # Simulate what an API would do - re-encode the deskewed image to send back as a response
    result, img_buf = cv2.imencode('.png', deskewed_img)
    img_bytes = img_buf.tobytes()

    # Simulate receiving the API response by reading the bytes back into an image
    img_deskewed = Image.open(BytesIO(img_bytes))

    return np.asarray(img_deskewed)


def deskew_image(image: np.ndarray) -> np.ndarray:
    """
    Deskew the given image.

    Parameters:
    - image (np.ndarray): The input image to deskew.

    Returns:
    - np.ndarray: The deskewed image.
    """
    # Convert to grayscale and invert
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    # Threshold the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Find the image moment
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
    
    # Determine the angle to deskew the image
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # Rotate the image to deskew it
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Compute the rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated

if __name__ == "__main__":
    img_path = './test_img.png'
    # Read the image from disk
    img = cv2.imread(img_path)

    if img is None:
        raise FileNotFoundError(f"The image at path {img_path} does not exist or is not readable.")
    
    # Deskew and save the image
    deskewed_img = deskew_image(img)
    cv2.imwrite('deskewed_img.png', deskewed_img)
    
