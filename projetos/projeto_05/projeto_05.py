# --- Imports --- #
import argparse
import time

import cv2
import imutils
import numpy as np
from imutils.video import VideoStream

# --- Constantes --- #
PROTOTXT = '../data/models/deploy.prototxt'
MODEL = '../data/models/res10_300x300_ssd_iter_140000.caffemodel'
CONFIDENCE_THRESHOLD = 0.7
POSITION = (200, 200)


def load_model(model_path: str, config_path: str) -> cv2.dnn_Net:
    """
    Carrega um modelo de rede neural pré-treinado.

    Parâmetros:
        model_path (str): Caminho para o arquivo contendo o modelo pré-treinado.

    Retorno:
        cv2.dnn_Net: Modelo pré-treinado de detecção de rostos no formato Caffe.

    Exemplo:
        model = load_model(model_path)
    """
    # Carrega o modelo
    model = cv2.dnn.readNetFromCaffe(config_path, model_path)

    return model


def detect_faces(model: cv2.dnn_Net, frame: np.ndarray) -> np.ndarray:
    """
    Detecta rostos em uma imagem utilizando um modelo de rede neural pré-treinado.

    Parâmetros:
        model (cv2.dnn_Net): Modelo pré-treinado de detecção de rostos no formato Caffe.
        frame (np.ndarray): Imagem de entrada onde os rostos serão detectados.

    Retorno:
        np.ndarray: Matriz contendo as detecções, onde cada detecção é representada por uma linha
                    contendo informações como as coordenadas do retângulo delimitador e a
                    confiança da detecção.

    Exemplo:
        detections = detect_faces(model, frame)
    """
    # Cria um blob a partir da imagem
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0)
    )

    # Define o blob como entrada para o modelo
    model.setInput(blob)

    # Executa uma passagem para frente (forward pass) através do modelo
    detections = model.forward()

    return detections


def process_detections(
    detections: np.ndarray,
    frame: np.ndarray,
    confidence_threshold: float = 0.5,
) -> np.ndarray:
    """
    Processa as detecções retornadas pelo modelo de detecção de rostos, desenhando os retângulos
    delimitadores e adicionando as informações de confiança.

    Parâmetros:
        detections (np.ndarray): Matriz contendo as detecções, onde cada detecção é representada por uma linha
                                 contendo informações como as coordenadas do retângulo delimitador e a
                                 confiança da detecção.
        frame (np.ndarray): Imagem de entrada onde os rostos foram detectados.
        confidence_threshold (float): Limiar de confiança para considerar uma detecção válida.

    Retorno:
        np.ndarray: Matriz contendo as detecções processadas, onde cada detecção é representada por uma linha
                    contendo informações como as coordenadas do retângulo delimitador e a
                    confiança da detecção.

    Exemplo:
        detections = process_detections(detections, frame)
    """
    # Obtém as dimensões da imagem
    (h, w) = frame.shape[:2]

    # Itera sobre as detecções
    for i in range(detections.shape[2]):
        # Obtém a confiança da detecção
        confidence = detections[0, 0, i, 2]

        # Verifica se a confiança é maior que o limiar
        if confidence > confidence_threshold:
            # Obtém as coordenadas do retângulo delimitador
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])

            # Converte as coordenadas para inteiros
            (startX, startY, endX, endY) = box.astype('int')

            kW = int(w / 3.0)
            kH = int(h / 3.0)
            face = frame[startY:endY, startX:endX]

            # blured = cv2.GaussianBlur(face, (kW, kH), 0)
            blured = anonymize_face_pixelate(face)

            frame[startY:endY, startX:endX] = blured

    return frame


def anonymize_face_pixelate(frame: np.ndarray, blocks: int = 9) -> np.ndarray:
    """
    Pixeliza uma face na imagem fornecida dividindo a imagem em blocos NxN e substituindo cada bloco
    pela média de suas cores. Esta função foi inspirada no trabalho de Adrian Rosebrock do site PyImageSearch.
    https://www.pyimagesearch.com

    Parâmetros:
        frame (np.ndarray): Imagem de entrada que terá uma face pixelizada.
        blocks (int): Número de blocos ao longo das dimensões da imagem. Quanto maior o número, menos
                      pixelizada a face aparecerá. O padrão é 9.

    Retorno:
        np.ndarray: Imagem com a face pixelizada.

    Exemplo:
        img_pixelizada = anonymize_face_pixelate(img_original, blocks=10)
    """
    # divide a imagem de entrada em blocos NxN
    (h, w) = frame.shape[:2]
    xSteps = np.linspace(0, w, blocks + 1, dtype='int')
    ySteps = np.linspace(0, h, blocks + 1, dtype='int')

    # loop sobre os blocos nas direções x e y
    for i in range(1, len(ySteps)):
        for j in range(1, len(xSteps)):
            # calcula as coordenadas de início e fim (x, y) para o bloco atual
            startX = xSteps[j - 1]
            startY = ySteps[i - 1]
            endX = xSteps[j]
            endY = ySteps[i]

            # extrai a ROI usando slicing de array NumPy, calcula a média da ROI,
            # e então desenha um retângulo com os valores médios RGB sobre a ROI na imagem original
            roi = frame[startY:endY, startX:endX]
            (B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
            cv2.rectangle(frame, (startX, startY), (endX, endY), (B, G, R), -1)

    # retorna a imagem com a face pixelizada
    return frame


if __name__ == '__main__':
    # constrói o parser de argumentos para receber o id da webcam
    ap = argparse.ArgumentParser()
    ap.add_argument(
        '-i',
        '--input',
        type=int,
        default=1,
        help='ID da webcam a ser utilizada',
    )
    args = vars(ap.parse_args())

    # carrega o modelo de detecção de rostos
    model = load_model(MODEL, PROTOTXT)

    # inicializa o stream de vídeo
    print('[INFO] Inicializando stream de vídeo...')
    vs = VideoStream(src=args['input']).start()
    time.sleep(2.0)

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)

        # detecta rostos na imagem
        detections = detect_faces(model, frame)

        # processa as detecções e pixeliza a face
        frame = process_detections(detections, frame, CONFIDENCE_THRESHOLD)

        # exibe a imagem
        cv2.imshow('Frame', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    vs.stop()
