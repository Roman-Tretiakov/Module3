def print_params(a=1, b='string', c=True):
    print(a, b, c)


values_list = ['list', False, 100]
values_list_2 = ['list', False]
values_dict = {'a': True, 'b': 'dictionary', 'c': 1000}

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)