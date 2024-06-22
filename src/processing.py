def filter_by_state(list_key: list, state: str = "EXECUTED") -> list:
    """Функция принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение."""
    filter_list = []
    for el in list_key:
        if el.get("state") == state:
            filter_list.append(el)
    return filter_list


def sort_by_date(date: list, reverse_key: bool = True) -> list:
    """Функция которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date).
    Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание)."""
    sort_date = sorted(date, key=lambda dict: dict["date"], reverse=reverse_key)
    return sort_date
