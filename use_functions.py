
account = 0
history = {}


while True:
    print('Главное меню')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню  --> ')
    if choice == '1':
        deposit = int(input('Введите сумму: '))
        account += deposit
        print(f'Баланс счета: {account} рублей')
        pass
    elif choice == '2':
        purchase_sum = int(input('Введите стоимость покупки: '))
        if purchase_sum > account:
            print('Средств не достатончо!')
        else:
            purchase_name = input('Введите название покупки: ')
            account -= purchase_sum
            history[purchase_name] = purchase_sum
            print(purchase_name, purchase_sum)
            print(f'Баланс счета: {account} рублей')
        pass
    elif choice == '3':
        print(history)
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
