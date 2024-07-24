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
    input_user = input("Введите слово для поиска: ")
    print(search_transaction_data(transaction_data, input_user))

