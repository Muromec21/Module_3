data_structure = [[1, 2, 3],
       {'a': 4, 'b': 5},
       (6, {'cube': 7, 'drum': 8}),
       "Hello",
       ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(css):

    a = 0

    if isinstance(css, int):
        return css

    elif isinstance(css, str):
        return len(css)

    elif isinstance(css, list):
        for i in css:
             a += calculate_structure_sum(i)
        return a

    elif isinstance(css, tuple):
        for i in css:
            a += calculate_structure_sum(i)
        return a

    elif isinstance(css,set):
        for i in css:
            a += calculate_structure_sum(i)
        return a

    elif isinstance(css, dict):
        for k in css.items():
            a += calculate_structure_sum(k)
        return a

    else:
        return 0




print(calculate_structure_sum(data_structure))
