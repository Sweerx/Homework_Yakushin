def get_mask_card_number(card_info: list) -> str:
    """
    Функция принимает на вход информацию о карте и возвращает зашифрованную информацию
    """
    # Шифруем номер карты
    card_info[-1] = f"{card_info[-1][:6]}******{card_info[-1][-4:]}"

    # Оборачиваем номер карты в список для перебора и вставки пробелов
    list_card_number = list(card_info[-1])
    counter = 0
    for index in range(1, len(list_card_number)):
        if index % 4 == 0:
            list_card_number.insert(index + counter, " ")
            counter += 1
    # Заменяем исходную строку с номером карты на зашифрованную с пробелами
    else:
        card_info[-1] = "".join(list_card_number)

    return " ".join(card_info)


def get_mask_account(account: list) -> str:
    """
    Функция принимает на вход информацию о счете и возвращает зашифрованную информацию
    """
    account[-1] = f"**{account[-1][-2:]}"

    return " ".join(account)
