import numpy as np


def index_like(arr: any, start: int = 0) -> np.ndarray:
    length = len(arr)
    index_s = np.arange(length)+start
    return index_s
