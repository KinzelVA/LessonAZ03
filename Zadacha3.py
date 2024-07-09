import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла prices.csv
df = pd.read_csv('prices.csv')

# Очистка данных: удаление символов и преобразование в числовой формат
df['Цена'] = df['Цена'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# Вычисление средней цены
mean_price = df['Цена'].mean()
print(f"Средняя цена: {mean_price}")

# Создание гистограммы цен
plt.hist(df['Цена'], bins=30, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')

# Показ гистограммы
plt.show()
