import argparse
from datetime import datetime, timedelta

def parse_date(day_number=None, day_of_week=None, month=None):
    try:
        # Получаем текущий год
        current_year = datetime.now().year

        # Получаем текущую дату
        current_date = datetime.now()

        # Если не указаны параметры, берем текущий день
        if day_number is None and day_of_week is None and month is None:
            return current_date

        # Если указан только номер дня, берем текущий месяц и текущий день недели
        if day_number is not None and day_of_week is None and month is None:
            first_day_of_month = current_date.replace(day=1)
            target_day = first_day_of_month + timedelta(days=(day_number - 1) + (current_date.weekday() - first_day_of_month.weekday()) % 7)
            return target_day

        # Если указан только день недели, берем текущий месяц и указанный день недели
        if day_number is None and day_of_week is not None and month is None:
            first_day_of_month = current_date.replace(day=1)
            target_day = first_day_of_month + timedelta(days=(current_date.weekday() - first_day_of_month.weekday() + (day_of_week - 1) * 7) % 7)
            return target_day

        # Если указан только месяц, берем первый день месяца и текущий день недели
        if day_number is None and day_of_week is None and month is not None:
            first_day_of_month = current_date.replace(month=month, day=1)
            target_day = first_day_of_month + timedelta(days=(current_date.weekday() - first_day_of_month.weekday()) % 7)
            return target_day

        # Если указаны все параметры, формируем дату
        if day_number is not None and day_of_week is not None and month is not None:
            first_day_of_month = datetime(current_year, month, 1)
            target_day = first_day_of_month + timedelta(days=(day_number - 1) + (day_of_week - first_day_of_month.weekday() + 7) % 7)
            return target_day

    except Exception as e:
        # Логируем ошибку, если текст не соответствует формату
        print(f"Ошибка при обработке параметров: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Преобразование текста в дату в текущем году.')
    parser.add_argument('--day_number', type=int, help='Номер дня в месяце')
    parser.add_argument('--day_of_week', type=int, choices=range(1, 8), help='Номер дня недели (1-пн, 2-вт, ..., 7-вс)')
    parser.add_argument('--month', type=int, choices=range(1, 13), help='Номер месяца (1-янв, 2-фев, ..., 12-дек)')

    args = parser.parse_args()

    result_date = parse_date(args.day_number, args.day_of_week, args.month)

    if result_date:
        print(result_date)
    else:
        print("Не удалось преобразовать параметры в дату.")

if __name__ == "__main__":
    main()









