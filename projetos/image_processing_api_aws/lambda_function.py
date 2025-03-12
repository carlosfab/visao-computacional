import json
import cv2
import base64
import numpy as np


def encode_image_to_base64(image_path):
    """
    Codifica uma imagem em Base64.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def decode_base64_to_image(base64_string, image_path="/tmp/decoded_image.png"):
    """
    Decodifica uma string Base64 para uma imagem e salva como PNG.
    """
    image_data = base64.b64decode(base64_string)
    with open(image_path, "wb") as f:
        f.write(image_data)
    return image_path
    

def lambda_handler(event, context):
    # Exemplo de como obter a string base64 da imagem a partir do evento
    base64_string = event['body']  # Adapte conforme a estrutura do seu evento

    # Decodifica a imagem para um arquivo temporário
    image_path = decode_base64_to_image(base64_string)

    # Lê a imagem decodificada usando OpenCV
    image = cv2.imread(image_path)

    # Processamento da imagem (exemplo: conversão para tons de cinza e inversão)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    # Continuação do processamento conforme necessário...

    # Codifica a imagem processada de volta para Base64 para retorno
    processed_image_base64 = encode_image_to_base64(image_path)

    # Retorna a imagem processada codificada em Base64
    return {
        'statusCode': 200,
        'isBase64Encoded': True,
        'headers': {'Content-Type': 'image/png'},
        'body': processed_image_base64
    }