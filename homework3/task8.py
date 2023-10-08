def guess_number():
    min_range = 1
    max_range = 100
    tries = 0

    while tries < 7:
        guess = (min_range + max_range) // 2
        print(f"Твое число равно, меньше или больше, чем {guess}?")
        response = int(input("Введите 1, если равно, 2, если больше, 3, если меньше: "))

        if response == 1:
            print(f"Компьютер угадал ваше число {guess}!")
            break
        elif response == 2:
            min_range = guess + 1
        elif response == 3:
            max_range = guess - 1
        else:
            print("Пожалуйста, введите 1, 2 или 3.")
            continue

        tries += 1

    if tries == 7:
        print("Компьютер не смог угадать число за 7 попыток.")

guess_number()
