from src.utils import get_financial_transactions, search_transaction_data, sorting_operations_category
import os


def main():

    print(f"Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:

        file_transaction_json = "1"
        file_transaction_csv = "2"
        file_transaction_xlsx = "3"

        print(
            f"Выберите необходимый пункт меню:\n"
            f"1. Получить информацию о транзакциях из JSON-файла\n"
            f"2. Получить информацию о транзакциях из CSV-файла\n"
            f"3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        user_file_choice = input(f"Введи необходимый пункт: ").strip()
        if user_file_choice == file_transaction_json:
            transaction_data = get_financial_transactions("operations.json")
            print(f"\nДля обработки выбран JSON-файл\n")
            break

        elif user_file_choice == file_transaction_csv:
            transaction_data = get_financial_transactions("transactions.csv")
            print(f"\nДля обработки выбран CSV-файл\n")
            break

        elif user_file_choice == file_transaction_xlsx:
            transaction_data = get_financial_transactions("transactions_excel.xlsx")
            print(f"\nДля обработки выбран XLSX-файл\n")
            break

        else:
            print(f"\nНекоректный выбор, попробуйте еще раз\n")
            continue

    print(
        f"Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
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
                f"Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )
            continue

    print(f'Отсортировать операции по дате? Да/Нет\n')

    while True:

        status_sort_yes_date = 'да'
        status_sort_no_date = 'нет'

        user_choice_sort_date = input('').lower()

        if user_choice_sort_date == status_sort_yes_date:
            break
        elif user_choice_sort_date == status_sort_no_date:
            break
        else:
            print(f'\nВыберите Да или Нет\n')

    print(f'\nОтсортировать по возрастанию или по убыванию?\n(по возрастанию/по убыванию)\n')

    while True:

        status_sort_ascending = 'по возрастанию'
        status_sort_descending = 'по убыванию'

        user_choice_sort_ascending_or_descending = input('').lower()

        if user_choice_sort_ascending_or_descending == status_sort_ascending:
            break
        elif user_choice_sort_ascending_or_descending == status_sort_descending:
            break
        else:
            print(f'\nВыберите по возрастанию/по убыванию\n')


    print(f'\nВыводить только рублевые тразакции? Да/Нет\n')

    while True:

        transaction_only_rub_yes = 'да'
        transaction_only_rub_no = 'нет'

        user_choice_transaction_only_rub = input('').lower()

        if user_choice_transaction_only_rub == transaction_only_rub_yes:
            break
        elif user_choice_sort_date == transaction_only_rub_no:
            break
        else:
            print(f'\nВыберите Да или Нет\n')

    print(f'\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n')

    while True:

        filter_for_description_yes = 'да'
        filter_for_description_no = 'нет'

        user_choice_filter_for_description = input('').lower()

        if user_choice_filter_for_description == filter_for_description_yes:
            break
        elif user_choice_filter_for_description == filter_for_description_no:
            break
        else:
            print(f'\nВыберите Да или Нет\n')

    print(f'\nРаспечатываю итоговый список транзакций...')






if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]

    # transaction_data = get_financial_transactions("operations.json")
    # transaction_data1 = get_financial_transactions("transactions.csv")
    # transaction_data2 = get_financial_transactions("transactions_excel.xlsx")

    # input_user = input("Введите слово для поиска: ")
    # print(search_transaction_data(transaction_data, input_user))

    # new_list = []
    # for el in search_transaction_data(transaction_data1, input_user):
    #     if el['description']:
    #         new_list.append(el['description'])
    # print("\n".join(map(str, new_list)))

    # print(sorting_operations_category(transaction_data2, categories_operations))

    main()
