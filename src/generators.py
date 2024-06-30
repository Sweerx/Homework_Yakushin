from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """
    Функция которая принимает список словарей с банковскими операциями
    (или объект-генератор, который выдает по одной банковской операции)
     и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    """Функция который принимает список словарей и
    возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction["description"]
