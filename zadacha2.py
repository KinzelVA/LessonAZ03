import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
data1 = np.random.rand(num_samples)
data2 = np.random.rand(num_samples)

# Создание диаграммы рассеяния
plt.scatter(data1, data2, alpha=0.5, edgecolors='w', s=50)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('Набор данных 1')
plt.ylabel('Набор данных 2')

# Показ диаграммы
plt.show()
