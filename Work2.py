# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс
# Используйте форматирование строк.
while True:
    time = input('Введите время в секундах\n')
    if time.isdigit():
        hour = int(time)//60**2
        while hour > 24:
            hour -= 24
        if hour < 10:
            hour = '0{}'.format(hour)
        min = int(time)%60**2//60
        if min < 10:
            min = '0{}'.format(min)
        sec = int(time)%60**2%60
        if sec < 10:
            sec = '0{}'.format(sec)
        print('{}:{}:{}'.format(hour, min, sec))
        break
    else:
        print('Некорректное время')