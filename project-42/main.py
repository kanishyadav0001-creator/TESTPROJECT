import numpy as np

Reshape = np.arange(9, dtype=np.float32).reshape(3, 3)
print('First array:')
print(Reshape)
print('\n')

b = np.array([10, 10, 10], dtype=np.float32)
print('Second array:')
print(b)
print('\n')

print('Add the two arrays:')
print(np.add(Reshape, b))
print('\n')

print('Subtract the two arrays:')
print(np.subtract(Reshape, b))
print('\n')

print('Multiply the two arrays:')
print(np.multiply(Reshape, b))
print('\n')

print('Divide the two arrays:')
print(np.divide(Reshape, b))
print('\n')