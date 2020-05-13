# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

while True:
    revenue = input('Введите выручку\n')
    costs = input('Введите затраты\n')
    if revenue.isdigit() and costs.isdigit():
        if int(revenue) > int(costs):
            profit = int(revenue) - int(costs)
            print('Ваша прибыль: {}'.format(profit))
            print('Рентабильность: {}%'.format(profit/int(revenue)*100))
            while True:
                employee = input('Введите количество сотрудников фирмы\n')
                if employee.isdigit():
                    print('прибыль фирмы в расчете на одного сотрудника: {}'.format(profit/int(employee)))
                    break
                else:
                    print('Некорректное число')
        else:
            loss = int(costs) - int(revenue)
            print('Ваш убыток: {}'.format(loss))
        break
    else:
        print('Некорректное число')