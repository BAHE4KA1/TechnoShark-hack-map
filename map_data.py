import osmnx as ox
import pandas as pd
import time

# Указываем название города
place_name = 'Краснодар, Россия'

# Функция для получения графа и обработки ошибок
def get_streets(place_name):
    for attempt in range(5):  # Попробуем 5 раз
        try:
            # Получаем граф улиц города
            graph = ox.graph_from_place(place_name, network_type='drive')
            return graph
        except Exception as e:
            print(f"Ошибка: {e}. Повторная попытка через 5 секунд...")
            time.sleep(5)  # Ждем 5 секунд перед повторной попыткой
    return None

# Получаем граф улиц
graph = get_streets(place_name)

if graph is not None:
    # Получаем данные о всех улицах в виде GeoDataFrame
    streets = ox.graph_to_gdfs(graph, nodes=False, edges=True)

    # Сохраняем информацию о улицах в таблицу
    streets_info = streets.columns()

    # Выводим информацию о улицах
    print(streets_info)

else:
    print("Не удалось получить граф улиц после нескольких попыток.")