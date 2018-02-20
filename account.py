def calculate_income(rate, money, month):
    if money <= 0:
        return 0

    for i in range(1, month + 1):
        money = round(money + money * rate / 100 / 12, 2)
    return money


def main():
    rate = 10
    money = 100000
    period = 12

    result = calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result)


if __name__ == "__main__":
    main()