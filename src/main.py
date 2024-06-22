from src.widget import mask_account_card, get_data

if __name__ == '__main__':
    print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
    print(mask_account_card("Maestro 1596 8378 6870 5199"))
    print(mask_account_card("MasterCard 7158 3007 3472 6758"))
    print(mask_account_card("Visa Classic 6831 9824 7673 7658"))
    print(mask_account_card("Счет 35383033474447895560"))

    print(get_data("2018-07-11T02:26:18.671407"))