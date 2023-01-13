year = input('Введите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Введите день рождения Пушкина:')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')

def true_number():
    day = input('Введите день рождения Пушкина:')
    while day != '6':
        print("Не верно")
        day = input('В какой день июня родился Пушкин?')
        return print('Верно')
true_number()