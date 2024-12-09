calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in (i.upper() for i in list_to_search)


print(string_info('Алексей Николаевич'))
print(string_info('Петр Васильевич'))
print(is_contains('Привет', ['Здравствуйте', 'Добрый день', 'пРиВеТ']))
print(is_contains('Мужчина', ['Женщина', 'Мужчины', 'Ребенок']))
print(calls)