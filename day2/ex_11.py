import math

import numpy as np

# pip install numpy

# ndarray - tablice, macierze
array = np.array([10, 100, 1000.])
print(array)  # [  10.  100. 1000.] kropka oznacza float
print(array.dtype)  # float64

array2 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(array2)
# [[1 2 3]
#  [4 5 6]]
print(array2.dtype)  # int64

# rzutowanie na typ pythonowy
print(float(array[0]))  # 10.0
print(type(float(array[0])))  # <class 'float'>

# dane typu json
# {"name":"John"}
import json

# dane z numpy
x = np.int64(64)
print(type(x))  # <class 'numpy.int64'>

# serializacja danych - zamina na json
# json.dumps(x)  # TypeError: Object of type int64 is not JSON serializable
python_int = int(x)
json_str = json.dumps({'value': python_int})
print(json_str)  # {"value": 64}

# broadcasting
# [[1 2 3]
#  [4 5 6]]

print(array2 + 1)
# [[2 3 4]
#  [5 6 7]]

print(array2 * array2)
# [[ 1  4  9]
#  [16 25 36]]

print(math.sqrt(25))  # 5.0

# print(math.sqrt(array2))  # TypeError: only length-1 arrays can be converted to Python scalars

# numpy posiada swoje metody
print(np.sqrt(array2))
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]]

# sumowanie elemntów tablicy
print(array2.sum())  # 21
