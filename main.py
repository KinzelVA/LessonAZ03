import pandas as pd

# Чтение данных из файла produkt.csv
df = pd.read_csv('produkt.csv')

# Оставление только столбца с ценами
prices_df = df[['Цена']]

# Сохранение данных в новый файл prices.csv
prices_df.to_csv('prices.csv', index=False)

print("Данные успешно сохранены в файл prices.csv")
