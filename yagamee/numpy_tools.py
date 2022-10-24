import numpy as np


def index_like(arr: any, start: int = 0) -> np.ndarray:
    length = len(arr)
    index_s = np.arange(length)+start
    return index_s


def text2mat(text: str) -> np.ndarray:
    data = []
    for row in text.split(";"):
        row_data = []
        for element_text in row.split():
            element = float(element_text)
            if element.is_integer():
                element = int(element)
            row_data.append(element)
        data.append(row_data)
    data_numpy = np.asarray(data)
    return data_numpy
