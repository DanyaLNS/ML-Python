 Аникин Данила
import torch
import numpy as np
import time

# Инициализация матриц и их размерности
n = 2000
A_CPU = torch.rand([n, n])
b_CPU = torch.rand([n, 1])
A_GPU = torch.rand([n, n]).cuda()
b_GPU = torch.rand([n, 1]).cuda()

# Убеждаемся, что объекты хранятся на цпу и гпу
print(f"A_CPU: {A_CPU.get_device()}")
print(f"b_CPU: {b_CPU.get_device()}")
print(f"A_GPU: {A_GPU.get_device()}")
print(f"b_GPU: {b_GPU.get_device()}")

# Решаем СЛАУ на ЦПУ
t0 = time.time()
x_CPU = torch.solve(b_CPU, A_CPU)
print (f"Code runtime is {time.time() - t0}")

# Решаем СЛАУ на ГПУ
t0 = time.time()
x_GPU = torch.solve(b_GPU, A_GPU)
print (f"Code runtime is {time.time() - t0}")
n = 5000
A_CPU = torch.rand([n, n])
b_CPU = torch.rand([n, 1])
A_GPU = torch.rand([n, n]).cuda()
b_GPU = torch.rand([n, 1]).cuda()

# Решаем СЛАУ на ЦПУ
t0 = time.time()
x_CPU = torch.solve(b_CPU, A_CPU)
print (f"Code runtime is {time.time() - t0}")

# Решаем СЛАУ на ГПУ
t0 = time.time()
x_GPU = torch.solve(b_GPU, A_GPU)
print (f"Code runtime is {time.time() - t0}")

n = 10000
A_CPU = torch.rand([n, n])
b_CPU = torch.rand([n, 1])
A_GPU = torch.rand([n, n]).cuda()
b_GPU = torch.rand([n, 1]).cuda()

# Решаем СЛАУ на ЦПУ
t0 = time.time()
x_CPU = torch.solve(b_CPU, A_CPU)
print (f"Code runtime is {time.time() - t0}")

# Решаем СЛАУ на ГПУ
t0 = time.time()
x_GPU = torch.solve(b_GPU, A_GPU)
print (f"Code runtime is {time.time() - t0}")
