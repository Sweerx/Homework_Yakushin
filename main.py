from src.utils import get_financial_transactions, search_transaction_data

if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]

    transaction_data = get_financial_transactions("operations.json")
    transaction_data1 = get_financial_transactions("transactions.csv")
    transaction_data2 = get_financial_transactions("transactions_excel.xlsx")
    # print(transaction_data[:6])
    # print('_______________________________')
    # print(transaction_data1[:6])
    print('_______________________________')
    # print(transaction_data2[:6])
    # print('_______________________________')
    input_user = input("Введите слово для поиска: ")
    # print(search_transaction_data(transaction_data1, input_user))
    new_list = []
    for el in search_transaction_data(transaction_data, input_user):
        if el['description']:
            new_list.append(el['description'])
    print("\n".join(map(str, new_list)))

