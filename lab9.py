import numpy as np

def longest_sequence(arr):

    # Вычисляет разницу между соседними элементами массива
    # Затем сравнивает каждую разницу с нулем, результат — булев массив
    equal_neighbors = np.diff(arr) == 0

    # Объединяем массивы в один. 
    # Выделяем нулем начало и конец каждой последовательности одинаковых элементов.
    equal_neighbors = np.concatenate(([0], equal_neighbors, [0]))

    # Преобразует булев массив в числовой
    changes = np.diff(equal_neighbors.astype(int))
    starts = np.where(changes == 1)[0]
    ends = np.where(changes == -1)[0]

    # Вычисляем длины каждой последовательности одинаковых элементов как разницу между индексами концов и начал
    lengths = ends - starts + 1
    max_length = lengths.max() if len(lengths) > 0 else 1

    return max_length

array = np.array([1, 1, 1, 2, 2, 5])
print("Longest sequence length:", longest_sequence(array))