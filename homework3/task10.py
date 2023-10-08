# Функция для определения, является ли дата магической
def is_magical_date(day, month, year):
    return day * month == year % 100

# Главная программа
def main():
    # Отображаем магические даты в XX веке
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, 32):
                if is_magical_date(day, month, year):
                    print(f"{day:02d}/{month:02d}/{year}")

if __name__ == "__main__":
    main()
