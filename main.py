# from src.generators import filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_data, mask_account_card
from src.utils import get_financial_transactions
from src.external_api import sum_transaction_amount

if __name__ == "__main__":
    # print(get_mask_card_number("Maestro 1596837868705199".split()))
    # print(get_mask_account("Счет 64686473678894779589".split()))
    # print(get_mask_card_number("MasterCard 7158300734726758".split()))
    # print(get_mask_account("Счет 35383033474447895560".split()))
    # print(get_mask_card_number("Visa Classic 6831982476737658".split()))
    # print(get_mask_card_number("Visa Platinum 8990922113665229".split()))
    # print(get_mask_card_number("Visa Gold 5999414228426353".split()))
    # print(get_mask_account("Счет 73654108430135874305".split()))
    #
    # print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
    # print(mask_account_card("Maestro 1596 8378 6870 5199"))
    # print(mask_account_card("MasterCard 7158 3007 3472 6758"))
    # print(mask_account_card("Visa Classic 6831 9824 7673 7658"))
    # print(mask_account_card("Счет 35383033474447895560"))
    #
    # print(get_data("2018-07-11T02:26:18.671407"))
    #
    # operations_list = [
    #     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    #     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    # ]
    # print(filter_by_state(operations_list))
    # print(filter_by_state(operations_list, "CANCELED"))
    #
    # print(sort_by_date(operations_list))
    # print(sort_by_date(operations_list, False))
    #
    #
    # transactions = [
    #     {
    #         "id": 939719570,
    #         "state": "EXECUTED",
    #         "date": "2018-06-30T02:08:58.425572",
    #         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод организации",
    #         "from": "Счет 75106830613657916952",
    #         "to": "Счет 11776614605963066702",
    #     },
    #     {
    #         "id": 142264268,
    #         "state": "EXECUTED",
    #         "date": "2019-04-04T23:20:05.206878",
    #         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 19708645243227258542",
    #         "to": "Счет 75651667383060284188",
    #     },
    #     {
    #         "id": 873106923,
    #         "state": "EXECUTED",
    #         "date": "2019-03-23T01:09:46.296404",
    #         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод со счета на счет",
    #         "from": "Счет 44812258784861134719",
    #         "to": "Счет 74489636417521191160",
    #     },
    #     {
    #         "id": 895315941,
    #         "state": "EXECUTED",
    #         "date": "2018-08-19T04:27:37.904916",
    #         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
    #         "description": "Перевод с карты на карту",
    #         "from": "Visa Classic 6831982476737658",
    #         "to": "Visa Platinum 8990922113665229",
    #     },
    #     {
    #         "id": 594226727,
    #         "state": "CANCELED",
    #         "date": "2018-09-12T21:27:25.241689",
    #         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
    #         "description": "Перевод организации",
    #         "from": "Visa Platinum 1246377376343588",
    #         "to": "Счет 14211924144426031657",
    #     },
    # ]
    #
    # usd_transactions = filter_by_currency(transactions, "USD")
    #
    # for _ in range(3):
    #     print(next(usd_transactions)["id"])
    #
    # descriptions = transaction_descriptions(transactions)
    #
    # for _ in range(5):
    #     print(next(descriptions))
    #
    #
    #
    # print(get_financial_transactions("operations.json"))
    # print(sum_transaction_amount(get_financial_transactions("operations.json")[0]))
    # print(sum_transaction_amount(get_financial_transactions("operations.json")[1]))
    # print(sum_transaction_amount(get_financial_transactions("operations.json")[2]))
    # print(get_financial_transactions('transactions.csv')[0:2])
    print(get_financial_transactions('transactions_excel.xlsx'))