def apply_all_func(int_list, *functions):
    func_dict = {}
    for func in functions:
        func_dict.update({func.__name__: func(int_list)})
    return func_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
