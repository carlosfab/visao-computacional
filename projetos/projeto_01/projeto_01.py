"""
Este script substitui o fundo verde em um vídeo (chroma key) por um vídeo ou imagem de fundo selecionada.

Uso:
    python projeto_01.py -i <video_entrada> -b <video_fundo>

Argumentos:
    -i, --input        Caminho para o vídeo de entrada com fundo verde.
    -b, --background   Caminho para o vídeo ou imagem de fundo que substituirá o fundo verde.

O script processa o vídeo de entrada quadro a quadro, identificando os pixels verdes usando uma faixa de cor especificada.
Em seguida, sobreponha essas áreas com os pixels correspondentes do vídeo ou imagem de fundo. O resultado é um novo
fluxo de vídeo exibido em tempo real onde o fundo verde original é substituído de forma contínua.

Pressione 'q' enquanto a janela de saída está em foco para encerrar o programa.

Exemplo:
    python projeto_01.py -i video_entrada.mp4 -b video_fundo.mp4
"""

import argparse

import cv2
import numpy as np

# Configura o argparse
parser = argparse.ArgumentParser(
    description='Script para substituição de fundo verde por uma imagem escolhida.'
)
parser.add_argument(
    '-i',
    '--input',
    help='Caminho para o vídeo com fundo verde.',
    required=True,
)
parser.add_argument(
    '-b', '--background', help='Caminho para o vídeo de fundo.', required=True
)
args = parser.parse_args()

# Carrega os dois vídeos
cap_webcam = cv2.VideoCapture(args.input)
cap_praia = cv2.VideoCapture(args.background)

# Loop principal
while True:
    # Lê um quadro de cada vídeo
    ret_webcam, frame_webcam = cap_webcam.read()
    ret_praia, frame_praia = cap_praia.read()

    # Verifica se os vídeos terminaram
    if not ret_webcam or not ret_praia:
        break

    # Define os limites da cor verde em RGB
    lower_green = np.array([0, 100, 0], dtype=np.uint8)
    upper_green = np.array([100, 255, 100], dtype=np.uint8)

    # Cria uma máscara com os pixels que estão dentro da faixa de cor verde
    mask = cv2.inRange(frame_webcam, lower_green, upper_green)

    # Usa a máscara para extrair os pixels da praia que correspondem ao fundo verde da webcam
    praia_background = cv2.bitwise_and(frame_praia, frame_praia, mask=mask)

    # Inverte a máscara para obter os pixels que não estão na faixa de cor verde
    mask_inv = np.invert(mask)

    # Usa a máscara invertida para extrair os pixels da webcam que não são verdes
    webcam_foreground = cv2.bitwise_and(
        frame_webcam, frame_webcam, mask=mask_inv
    )

    # Combina o primeiro plano da webcam e o fundo da praia
    result = cv2.addWeighted(praia_background, 1, webcam_foreground, 1, 0)

    # Exibe o resultado
    cv2.imshow('Result', result)

    # Verifica se a tecla 'q' foi pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Quando tudo estiver pronto, libera a captura e fecha todas as janelas
cap_webcam.release()
cap_praia.release()
cv2.destroyAllWindows()


