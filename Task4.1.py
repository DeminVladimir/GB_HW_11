# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


values = input('Введите ключевые параметры в виде "значение"/"значение"/...:(Значение вводите без "") ').split('/')
result = {}

for i in values:
    try:
        result[int(i)] = int
        continue
    except:
        pass
    try:
        result[float(i)] = float
        continue
    except:
        pass
    if i == 'None':
        result[None] = None
        continue
    if '[' and ']' in i:
        result[i] = list
        continue
    if '{' and '}' in i:
        result[i] = set
        continue
    if '(' and ')' in i:
        result[i] = tuple
        continue
    if i == 'True' or i == 'False':
        result[i] = bool
        continue
    else:
        result[i] = type(i)

print(result)