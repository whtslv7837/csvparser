import csv

def csv_reader(paths):
    data = []

    for path in paths:
        try:
            with open(path, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data.extend(reader)
        except FileNotFoundError:
            raise SystemExit(f'Ошибка: файл {path} не найден')

    return data