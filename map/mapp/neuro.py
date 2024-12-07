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