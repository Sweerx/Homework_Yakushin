# Проект Homework_Yakushin

## Описание:

Проект Homework_Yakushin - нужен для обучения и сдачи домашнего задания.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Sweerx/Homework_Yakushin.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Что делают функции:
## src/widget.py
```
mask_account_card - Функция принимает строку с информацией — тип карты/счета и номер карты/счета
    Возвращать исходную строку с замаскированным номером карты/счета.

get_data - Функция прнимает зашифрованню строку(2018-07-11T02:26:18.671407) и возвращает дату
```

## src/processing.py
```
filter_by_state - Функция фильтрации операций по ключу state

sort_by_date - Функция сортировки операций по дате
```