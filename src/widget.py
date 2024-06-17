def mask_account_card(text: str) -> str:
    """Функция принимает строку с информацией — тип карты/счета и номер карты/счета
    Возвращать исходную строку с замаскированным номером карты/счета."""
    new_text_list = text.split()
    if len(new_text_list) > 2:
        num_card_str = new_text_list[2]
        num_card_one_block = num_card_str[:4]
        num_card_two_block = num_card_str[4:8].replace(num_card_str[6:8], "*" * 2)
        num_card_three_block = num_card_str[8:12].replace(num_card_str[8:12], "*" * 4)
        num_card_four_block = num_card_str[12:16]
        num_mask_card_len_3 = (
            new_text_list[0]
            + " "
            + new_text_list[1]
            + " "
            + num_card_one_block
            + " "
            + num_card_two_block
            + " "
            + num_card_three_block
            + " "
            + num_card_four_block
        )
        return num_mask_card_len_3
    elif new_text_list[0] != "Счет":
        num_card_str = new_text_list[1]
        num_card_one_block = num_card_str[:4]
        num_card_two_block = num_card_str[4:8].replace(num_card_str[6:8], "*" * 2)
        num_card_three_block = num_card_str[8:12].replace(num_card_str[8:12], "*" * 4)
        num_card_four_block = num_card_str[12:16]
        num_mask_card = (
            new_text_list[0]
            + " "
            + num_card_one_block
            + " "
            + num_card_two_block
            + " "
            + num_card_three_block
            + " "
            + num_card_four_block
        )
    else:
        num_account_str = new_text_list[1]
        num_mask_account = num_account_str[-6:].replace(num_account_str[-6:-4], "*" * 2)
        return new_text_list[0] + " " + num_mask_account

    return num_mask_card


def get_data(text: str) -> str:
    """Функция прнимает зашифрованню строку(2018-07-11T02:26:18.671407) и возвращает дату"""
    new_string = text.split("-")
    data_string = new_string[2][0:2] + "." + new_string[1] + "." + new_string[0]
    return data_string
