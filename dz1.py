def task1(day, month, year):
    # задача 1
    name_month = {'1': 'января', '2': 'февраля', '3': 'марта',
                  '4': 'апреля', '5': 'мая', '6': 'июня',
                  '7': 'июля', '8': 'августа', '9': 'сентября',
                  '10': 'октября', '11': 'ноября', '12': 'декабря'}
    return f'{day} {name_month[month]} {year} года'


def task2(names):
    # задача 2
    answer = {}
    for i in names:
        count = names.count(i)
        answer[i] = count
    return answer


def task3(name):
    # задача 3
    first = name.get('first_name')
    middle = name.get('middle_name')
    last = name.get('last_name')
    if last is not None and first is not None and middle is not None:
        return name['last_name'], name['first_name'], name['middle_name']
    elif last is None and middle is not None and first is not None:
        return name['middle_name'], name['first_name']
    elif middle is None and last is not None:
        if first is not None:
            return name['last_name'], name['first_name']
        else:
            return name['last_name']
    elif first is None and last is not None:
        return name['last_name']
    elif first is None and last is None:
        return 'Нет данных'


def task4(num):
    # задача 4
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))


def task5(*args):
    # задача 5
    ans = []
    for i in args:
        if (isinstance(i, int) or isinstance(i, float)) \
                and ans.count(i) != 1 and not isinstance(i, bool):
            ans.append(i)
    ans.sort()
    return ans
