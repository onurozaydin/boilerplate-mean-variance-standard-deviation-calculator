import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.reshape(lst, (3, 3))
    calculations = {
        'mean': [
            list(matrix.mean(axis=0)),
            list(matrix.mean(axis=1)),
            np.mean(matrix)
        ],
        'variance': [
            list(matrix.var(axis=0)),
            list(matrix.var(axis=1)),
            np.var(matrix)
        ],
        'standard deviation': [
            list(matrix.std(axis=0)),
            list(matrix.std(axis=1)),
            np.std(matrix)
        ],
        'max': [
            list(matrix.max(axis=0)),
            list(matrix.max(axis=1)),
            np.max(matrix)
        ],
        'min': [
            list(matrix.min(axis=0)),
            list(matrix.min(axis=1)),
            np.min(matrix)
        ],
        'sum': [
            list(matrix.sum(axis=0)),
            list(matrix.sum(axis=1)),
            np.sum(matrix)
        ]
    }
    return calculations
