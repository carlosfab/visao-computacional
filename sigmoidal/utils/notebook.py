from typing import List, Optional, Tuple

import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_image(
        image: np.ndarray,
        size: Tuple[int, int] = (10, 10),
        cmap: Optional[str] = 'gray'
) -> None:
    """
    Exibe uma imagem carregada pelo OpenCV em um Jupyter notebook.

    Parâmetros:
        image (np.ndarray): Imagem a ser exibida.
        size (tuple): Tamanho da figura na qual a imagem será exibida (largura, altura).
        cmap (str): Mapa de cores a ser usado se a imagem for em escala de cinza.

    Retorno:
        None
    """
    plt.figure(figsize=size)

    if image.ndim == 2:
        plt.imshow(image, cmap=cmap)
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.axis("off")
    plt.show()
