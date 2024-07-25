from typing import Any

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_financial_transactions, search_transaction_data
from src.widget import get_data, mask_account_card


def main() -> Any:
    """Основная логина приложения"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:

        file_transaction_json = "1"
        file_transaction_csv = "2"
        file_transaction_xlsx = "3"

        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        user_file_choice = input("Введи необходимый пункт: ").strip()
        if user_file_choice == file_transaction_json:
            transaction_data = get_financial_transactions("operations.json")
            is_open_file = "json"
            print("\nДля обработки выбран JSON-файл\n")
            break

        elif user_file_choice == file_transaction_csv:
            transaction_data = get_financial_transactions("transactions.csv")
            is_open_file = "csv"
            print("\nДля обработки выбран CSV-файл\n")
            break

        elif user_file_choice == file_transaction_xlsx:
            transaction_data = get_financial_transactions("transactions_excel.xlsx")
            is_open_file = "xlsx"
            print("\nДля обработки выбран XLSX-файл\n")
            break

        else:
            print("\nНекоректный выбор, попробуйте еще раз\n")
            continue

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию. "
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    while True:
        status_filter_executed = "EXECUTED"
        status_filter_canceled = "CANCELED"
        status_filter_pending = "PENDING"

        user_choice_filter_status = input().upper()

        if user_choice_filter_status == status_filter_executed:
            print(f"\nОперации отфильтрованы по статусу {status_filter_executed}\n")
            break
        elif user_choice_filter_status == status_filter_canceled:
            print(f"\nОперации отфильтрованы по статусу {status_filter_canceled}\n")
            break
        elif user_choice_filter_status == status_filter_pending:
            print(f"\nОперации отфильтрованы по статусу {status_filter_pending}\n")
            break
        else:
            print(f'Статус операции "{user_choice_filter_status}" недоступен.\n')
            print(
                "Введите статус, по которому необходимо выполнить фильтрацию. "
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )
            continue

    print("Отсортировать операции по дате? Да/Нет\n")

    while True:

        status_sort_yes_date = "да"
        status_sort_no_date = "нет"

        user_choice_sort_date = input("").lower()

        if user_choice_sort_date == status_sort_yes_date:

            print("\nОтсортировать по возрастанию или по убыванию?\n(по возрастанию/по убыванию)\n")

            while True:

                status_sort_ascending = "по возрастанию"
                status_sort_descending = "по убыванию"

                user_choice_sort_ascending_or_descending = input("").lower()

                if user_choice_sort_ascending_or_descending == status_sort_ascending:
                    descending = False
                    break
                elif user_choice_sort_ascending_or_descending == status_sort_descending:
                    descending = True
                    break
                else:
                    print('\nВыберите "по возрастанию"/"по убыванию"\n')
            break
        elif user_choice_sort_date == status_sort_no_date:

            descending = True
            break
        else:
            print('\nВыберите "Да" или "Нет"\n')

    print("\nВыводить только рублевые тразакции? Да/Нет\n")

    while True:

        transaction_only_rub_yes = "да"
        transaction_only_rub_no = "нет"

        user_choice_transaction_only_rub = input("").lower()

        if user_choice_transaction_only_rub == transaction_only_rub_yes:
            is_only_rub_transaction = True
            break
        elif user_choice_transaction_only_rub == transaction_only_rub_no:
            is_only_rub_transaction = False
            break
        else:
            print('\nВыберите "Да" или "Нет"\n')

    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n")

    while True:

        filter_for_description_yes = "да"
        filter_for_description_no = "нет"

        user_choice_filter_for_description = input("").lower()

        if user_choice_filter_for_description == filter_for_description_yes:
            user_choice_filter_for_description_status = input("\nВведите строку описания: \n")
            break
        elif user_choice_filter_for_description == filter_for_description_no:
            user_choice_filter_for_description_status = ""
            break
        else:
            print('\nВыберите "Да" или "Нет"\n')

    print("\nРаспечатываю итоговый список транзакций...\n")

    result_state = filter_by_state(transaction_data, user_choice_filter_status)  # Фильтрация по статусу
    result_sort_date_state = sort_by_date(result_state, descending)  # Сортировка по дате и по убывани/возрастанию
    result = search_transaction_data(
        result_sort_date_state, user_choice_filter_for_description_status
    )  # Фильтрует список по фразе в описании
    if is_only_rub_transaction:
        result = list(filter_by_currency(result, is_open_file, "RUB"))  # Только рублевые транзакции

    print(f"Всего банковских операций в выборке: {len(result)}\n")

    for res in result:
        print(get_data(res["date"]), res["description"])
        if res.get("from") and isinstance(res["from"], str):
            print(f"{mask_account_card(res['from'])} -> {mask_account_card(res['to'])}")
        else:
            print(f"{mask_account_card(res['to'])}")

        if is_open_file == "json":
            print(f'Сумма: {res["operationAmount"]["amount"]} {res['operationAmount']['currency']['name']}\n')

        elif is_open_file == "csv" or is_open_file == "xlsx":
            print(f'Сумма: {res["amount"]} {res['currency_name']}\n')

    if not result:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":

    main()
