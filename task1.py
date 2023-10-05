def powerset(x):
    p_x = set()
    list_x = list(x)
    x_len = len(list_x)
    for i in range(1 << x_len):
        bin_code = bin(i)[2:].zfill(x_len)
        subset = set()
        for j in range(x_len):
            if bin_code[j] == '1':
                subset.add(list_x[j])
        p_x.add(frozenset(subset))
    return p_x


def p(x):
    return powerset(x)


def sorter_powerset(item):
    return len(item), sorted(item)


def cartesian_product(x, y):
    return {(ix, iy) for ix in x for iy in y}


def set_to_str(x):
    return f'{{{", ".join([str(item) for item in sorted(x)])}}}'


def double_set_to_str(x):
    return f'{{{", ".join([set_to_str(subset) for subset in sorted(x, key=sorter_powerset)])}}}'


def print_binary_relation_matrix(x, y, g):
    if len(x) == 0 or len(y) == 0:
        return
    keys = sorted(x)
    len_key = len(max(map(str, [keys[0], keys[-1]])))
    values = sorted(y)
    len_value = len(max(map(str, [values[0], values[-1]])))
    print(' ' * len_key, end=' ')
    for value in values:
        print(str(value).rjust(len_value), end=' ')
    print('\r\n' + ' ' * len_key + ('┼' + '─' * len_value) * len(values) + '┼')
    for key in keys:
        print(str(key).rjust(len_key), end='│')
        for value in values:
            print(f'{1 if (key, value) in g else 0}'.rjust(len_value), end='│')
        print('\r\n' + ' ' * len_key + ('┼' + '─' * len_value) * len(values) + '┼')


def run():

    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 9, 10, 11, 12}
    c = {5, 6, 7, 8, 9, 10, 13, 14}

    d1 = b ^ c
    print('D_1:')
    print(set_to_str(d1), end='\r\n\r\n')

    pd1 = p(d1)
    print('P(D_1):')
    print(double_set_to_str(pd1), end='\r\n\r\n')

    d2 = a - (b | c)
    print('D_2:')
    print(set_to_str(d2), end='\r\n\r\n')

    d = cartesian_product(d1, d2)
    print('D:')
    print(set_to_str(d), end='\r\n\r\n')

    u = a | b | c
    print('<U, U, D>:')
    print_binary_relation_matrix(u, u, d)
