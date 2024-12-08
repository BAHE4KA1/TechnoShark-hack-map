from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat
auth_t = 'YWFlM2RmYmYtOWU4ZS00NDdjLTg4ZDItMDE0MWFhOWM3ZWZiOjBiYzNjN2RjLWZiZTUtNDkzZS04MTRlLTkxMGVkYzAxYzQ2Ng=='


def auth_llm(auth_t):
    llm = GigaChat(
        credentials=auth_t,
        scope="GIGACHAT_API_PERS",
        model="GigaChat",
        verify_ssl_certs=False,
        streaming=False,
    )

    return llm

def answer(req):
    llm = auth_llm(auth_t)

    messages = [SystemMessage(
        content="""
        Ты - бот для анализа данных о пробках. Ты будешь получать на вход запрос от прользователя в формате
        "{start_time} {traffic_value}" - в примерном виде "8:00 4"
        Ты должен будешь прогнозировать примерное время устранения пробки. Веса пробок слудующие:
        1-3 балла - 5-10 минут
        4-7 баллов - 10-30 минут
        8+ баллов - от 30 минут до неск. часов
        Вот пример твоей работы:
        Запрос: 8:00 2; Ответ: 8:10
        Запрос: 9:30 6; Ответ: 9:50
        Запрос: 15:00 10; Ответ: 17:00
        В ответ указывай ТОЛЬКО время в формате hh:mm и больше ничего
        """
    ), HumanMessage(content=req)]

    res = llm.invoke(messages)

    return res.content

# def data_get(model):
#     city_name = 'Краснодар'
#
#     graph = ox.graph_from_place(city_name, network_type='all')
#
#     gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)
#
#     streets = gdf_edges['name'].dropna().tolist()
#
#     a = []
#     for s in streets:
#         if type(s) == type([]):
#             for i in s:
#                 if i not in a: a.append(i)
#         else:
#             if s not in a: a.append(s)
#
#     streets = a
#
#     t = [f'{i}:00' for i in range(0, 24)]
#     t = t + [f'{i}:30' for i in range(0, 24)]
#
#     k = 10
#     for i in streets:
#         k -= 1
#         log = model(name=i, traffic_value=randint(1, 10), time_start=choice(t))
#         print(log)
#         if k == 0: break