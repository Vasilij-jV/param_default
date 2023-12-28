# -*- config: utf-8 -*-

# Функция с параметрами по умолчанию
def print_params(a=34, b='parameter with value string', c=True):
    return a, b, c

print(print_params())
print(print_params(2))
print(print_params(101, b='other string'))
print(print_params(b='one more line', c=False))
print(print_params(b=87))
print(print_params(c=[1, 2, 3]))

# Распаковка параметров

set_arg = {'10, 20'}
value_list = ['string', (2, 3), set_arg]
value_dist = {
    'a': False,
    'b': 34,
    'c': {
        'd': []
    }
}

print(print_params(*value_list))
print(print_params(**value_dist))

# Распаковка + отдельные параметры

value_list_2 = ['string', 56]
print(print_params(*value_list_2, 23))