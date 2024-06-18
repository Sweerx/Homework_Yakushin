def mask_account_card(text: str) -> str:
    """Функция принимает строку с информацией — тип карты/счета и номер карты/счета
    Возвращать исходную строку с замаскированным номером карты/счета."""
    new_text = text.split()
    name_cards = []
    for el in new_text:
        if el.isalpha():
            name_cards.append(el)

    if len(new_text) <= 2:
        num_account_str = new_text[1]
        num_mask_account = num_account_str[-6:].replace(num_account_str[-6:-4], "*" * 2)
        return new_text[0] + " " + num_mask_account

    else:
        num_card_str = new_text[-1] + new_text[-2] + new_text[-3] + new_text[-4]
        num_card_one_block = num_card_str[:4]
        num_card_two_block = num_card_str[4:8].replace(num_card_str[6:8], "*" * 2)
        num_card_three_block = num_card_str[8:12].replace(num_card_str[8:12], "*" * 4)
        num_card_four_block = num_card_str[12:16]

        if len(name_cards) >= 2:
            num_mask_card = (
                name_cards[0]
                + " "
                + name_cards[1]
                + " "
                + num_card_one_block
                + " "
                + num_card_two_block
                + " "
                + num_card_three_block
                + " "
                + num_card_four_block
            )
            return num_mask_card
        elif len(name_cards) <= 1:
            num_mask_card = (
                name_cards[0]
                + " "
                + num_card_one_block
                + " "
                + num_card_two_block
                + " "
                + num_card_three_block
                + " "
                + num_card_four_block
            )
            return num_mask_card
    return ""


def get_data(text: str) -> str:
    """Функция прнимает зашифрованню строку(2018-07-11T02:26:18.671407) и возвращает дату"""
    new_string = text.split("-")
    data_string = new_string[2][0:2] + "." + new_string[1] + "." + new_string[0]
    return data_string


print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
