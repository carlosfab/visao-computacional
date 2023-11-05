from typing import List, Optional, Tuple

import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_images_grid(
    images: List[np.ndarray],
    grid_size: Tuple[int, int],
    titles: Optional[List[str]] = None,
    size: Tuple[int, int] = (10, 10),
    cmap: str = 'gray',
) -> None:
    """
    Display a grid of images with optional titles.

    Parameters
    ----------
    images : List[np.ndarray]
        A list of images to be displayed. Each image should be a NumPy array.

    grid_size : Tuple[int, int]
        A tuple specifying the number of rows and columns in the grid layout.

    titles : Optional[List[str]], default=None
        An optional list of titles for each subplot. The list should have the same length as `images`.

    size : Tuple[int, int], default=(10, 10)
        A tuple specifying the width and height of the entire plot figure.

    cmap : str, default='gray'
        The colormap used for displaying single-channel images.

    Raises
    ------
    ValueError
        If the number of images exceeds the total spots in the grid.

    Example
    -------
    >>> images = [np.random.rand(10, 10) for _ in range(4)]
    >>> plot_images_grid(images, grid_size=(2, 2), titles=['Img1', 'Img2', 'Img3', 'Img4'])

    Returns
    -------
    None
    """
    rows, cols = grid_size

    if len(images) > rows * cols:
        raise ValueError('Number of images exceeds grid size.')

    # Creating a figure with a specified size
    plt.figure(figsize=size)

    for i, img in enumerate(images):
        # Creating subplots
        plt.subplot(rows, cols, i + 1)

        # If the image is single channel (like grayscale), use the specified colormap
        if len(img.shape) == 2:
            plt.imshow(img, cmap=cmap)
        else:
            # Convert from BGR to RGB since OpenCV loads in BGR format
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Optional titles
        if titles is not None:
            plt.title(titles[i])

        # Removing x and y ticks
        plt.xticks([])
        plt.yticks([])

    plt.show()


def plot_image(
    image: np.ndarray,
    size: Tuple[int, int] = (5, 5),
    cmap: Optional[str] = 'gray',
) -> None:
    """
    Display an image loaded with OpenCV in a Jupyter notebook.

    Parameters
    ----------
    image : np.ndarray
        The image to be displayed.

    size : Tuple[int, int], default=(10, 10)
        The size of the figure in which the image will be displayed (width, height).

    cmap : Optional[str], default='gray'
        The colormap to be used if the image is grayscale.

    Returns
    -------
    None
    """
    plt.figure(figsize=size)

    if image.ndim == 2:
        plt.imshow(image, cmap=cmap)
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.axis('off')
    plt.show()
