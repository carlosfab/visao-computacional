"""
Este módulo contém um script para extrair cores RGB de um vídeo usando o OpenCV.

O script abre um arquivo de vídeo e exibe seus quadros. Quando o usuário clica em um pixel no quadro, o script
extrai a cor RGB daquele pixel e adiciona-a a uma lista de amostras de cores. Em seguida, o script calcula os limites
inferior e superior da faixa de cor com base nas amostras e exibe as informações de cor no quadro.

Uso:
    python identificar_cor.py -i <arquivo_video>

Argumentos:
    -i (--image): Caminho para o arquivo de vídeo.

Exemplo:
    python identificar_cor.py -i video.mp4
"""
import argparse

import cv2
import numpy as np

# Inicializa a lista de amostras
samples = []


# Função callback para o evento do mouse
def callback(event: int, x: int, y: int) -> None:
    """
    Função de callback a ser chamada quando um evento do mouse ocorre na janela da imagem.

    Esta função recupera a cor na localização do clique, adiciona-a a uma lista de amostras,
    calcula os limites inferior e superior da faixa de cor, e exibe as informações de cor na janela da imagem.

    Args:
        event (int): O tipo de evento do mouse que ocorreu.
        x (int): A coordenada x do evento do mouse.
        y (int): A coordenada y do evento do mouse.

    Returns:
        None
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # Recupera as cores na localização do clique
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]
        # Adiciona a cor à lista de amostras
        samples.append([blue, green, red])
        # Calcula os limites inferior e superior
        lower_bound = np.amin(samples, axis=0)
        upper_bound = np.amax(samples, axis=0)
        print(f'Lower bound: {lower_bound}')
        print(f'Upper bound: {upper_bound}')
        # Desenha as informações na tela
        text = f'B: {blue}, G: {green}, R: {red}'
        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            1,
        )
        cv2.imshow('image', frame)


# Configura o argparse
parser = argparse.ArgumentParser(
    description='Script para extrair cores RGB de um video.'
)
parser.add_argument(
    '-i', '--image', help='Caminho para o video.', required=True
)
args = parser.parse_args()

# Carrega o primeiro frame do video
cap = cv2.VideoCapture(args.image)
ret, frame = cap.read()
if not ret:
    print(f'Não foi possível abrir o video: {args.image}')
    exit(1)

cv2.namedWindow('image')
cv2.setMouseCallback('image', callback)

# Exibe a imagem até que o usuário pressione 'q' ou 'esc'
while True:
    cv2.imshow('image', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
