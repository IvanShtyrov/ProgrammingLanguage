# Ввод сопротивлений проводников
resistance1 = float(input("Введите сопротивление первого проводника: "))
resistance2 = float(input("Введите сопротивление второго проводника: "))
# Вычисление общего сопротивления в соответствии с формулой для соединения проводников в серии
total_resistance = resistance1 + resistance2
# Округление результата до 1 знака после запятой
total_resistance = round(total_resistance,1)
# Вывод результата
print(f"Общее сопротивление цепи: {total_resistance} Ом")
