# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

startsumm = 0
count = 1
while True:
    if startsumm > 5_000_000:
        print("Остаток на счете", startsumm * 0.9, "Вычтен налог на богатство = ", startsumm * 0.1)

    choice = input("Выберите операцию Пополнение 1 Снятие 2 Выход 3   ")
    if choice == '1':
        s = int(input("Внесите на счет сумму кратную 50 у.е. "))
        if s % 50 == 0 and count < 3:
            startsumm += s
            print(round(startsumm, 2), "на вашем счету")
            count += 1
        elif s % 50 == 0 and count == 3:
            startsumm += s
            print(round(startsumm * 1.03, 2), "на вашем счету")
        else:
            print("Такую сумму внести нельзя")

    if choice == '2':
        s1 = int(input("Снимите со счета сумму кратную 50 у.е. "))
        if s1 % 50 == 0 and count < 3 and s1 < startsumm:
            if s1 * 0.015 > 30 and s1 * 0.015< 600:
                startsumm -= s1 * 1.015
                print(round(startsumm, 2), "на вашем счету")
                count += 1
            if s1 * 0.015 < 30:
                startsumm -= s1 + 30
                print(round(startsumm, 2), "на вашем счету")
                count += 1
            if s1 * 0.015 > 600:
                startsumm -= s1 + 600
                print(round(startsumm, 2), "на вашем счету")
                count += 1
        elif s1 % 50 == 0 and count == 3 and s1 < startsumm:
            if s1 * 0.015 > 30 and s1 * 0.015 < 600:
                startsumm -= s1 * 1.015
                print(round(startsumm * 1.03, 2), "на вашем счету")
            if s1 * 0.015 < 30:
                startsumm -= s1 + 30
                print(round(startsumm * 1.03, 2), "на вашем счету")
                count += 1
            if s1 * 0.015 > 600:
                startsumm -= s1 + 600
                print(round(startsumm * 1.03, 2), "на вашем счету")
                count += 1
        elif s1 > startsumm or s1 % 50 != 0:
            print("Такую сумму снять нельзя")

    if choice == '3':
        break

