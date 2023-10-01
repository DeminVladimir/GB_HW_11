# Задача о банкомате из 2-го семинара
# Начальная сумма равна нулю +
# Допустимые действия: пополнить, снять, выйти +
# Сумма пополнения и снятия кратны 50 у.е. +
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. +
# После каждой третей операции пополнения или снятия начисляются проценты - 3% +
# Нельзя снять больше, чем на счёте +
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной +
# Любое действие выводит сумму денег +
# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции. +
# Дополнительно сохраняйте все операции поступления и снятия средств в список. +

bank = 0
count = 0
withdrawal_percentage = 0.015
income = 0.03
percentage_of_wealth = 0.01


the_history_of_operations = []

def add_bank(cash: float) -> None:
    global bank
    global count
    global the_history_of_operations
    bank += cash
    count += 1
    the_history_of_operations.append(cash)
    if count % 3 == 0:
        bank = bank + income * bank
        print(f'начислены проценты в размере: {round((income * bank), 2)} у.е.')


def wealth_tax():
    global bank
    global count
    if bank > 5_000_000:
        bank = bank - bank * percentage_of_wealth
        print(f'Списан налог на богатство: {round((bank * percentage_of_wealth), 2)} у.е.')

def take_bank(cash: float) -> None:
    global bank
    global count
    global the_history_of_operations
    bank -= cash
    count += 1
    the_history_of_operations.append(-cash)


    if cash*withdrawal_percentage < 30:
        bank -= 30
        print("списаны проценты за cash: ", 30, "у.е.")
    elif cash*withdrawal_percentage > 600:
        bank -= 600
        print("списаны проценты за cash: ", 600, "у.е.")
    else:
        bank -= cash * withdrawal_percentage
        print(f'списаны проценты за cash: {cash * withdrawal_percentage} у.е.')
    if count % 3 == 0:
        bank = bank + income * bank
        print(f'начислены проценты в размере: {round((income * bank), 2)} у.е.')


def exit_bank():
    print("Рады вас видетеь снова!")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50: "))
        if cash % 50 == 0:

            return cash


while True:
    action = input("1 - Снять деньги\n2 - Пополнить\n3 - Баланс\n5 - Просмотреть историю операций\n4 - Выйти\nЧто вы выбираете? \n")

    if action == '1':
        print('Вы выбрали снятие наличных')
        wealth_tax()
        cash = check_bank()
        if cash < bank:
            take_bank(cash)
        else:
            print(f'На вашем счету не достаточно средств. Ваш баланс {round((bank), 2)} у.е.')
        wealth_tax()
        print(f'Баланс = {round((bank), 2)} у.е.')
    elif action == '2':
        print('Вы выбрали пополнить счет')
        add_bank(check_bank())
        wealth_tax()
        print(f'Баланс = {round((bank), 2)} у.е.')
    elif action == '3':
        print('Вы выбрали проверить баланс вашего счета')
        print(f'Баланс = {round((bank), 2)} у.е.')
    elif action == '4':
        print(the_history_of_operations)
        print(f'Баланс = {round((bank), 2)} у.е.')
    elif action == '5':
        print('Вы выбрали выйти из вашего счета')
        print(f'Баланс = {round((bank), 2)} у.е.')
        exit_bank()
    else:
        print('Введен не верный выбор')