import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s", "%d.%m.%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(file_name: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях"""
    try:
        logger.info(f"Попытка открыть файл {file_name}")
        with open(os.path.join("data/", file_name), "r", encoding="utf-8") as f:
            logger.info(f"Файл {file_name} успешно открыт")
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Файл {file_name} успешно десериализован")
                return data
            else:
                logger.error(f"Файл {file_name} не содержит список")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {file_name} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {file_name} не содержит JSON-строки")
        return []
