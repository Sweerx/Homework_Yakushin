import json
import os


def get_financial_transactions(file_name: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях"""
    try:
        with open(os.path.join("data/", file_name), "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
