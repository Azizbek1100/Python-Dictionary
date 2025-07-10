def count_names(names: list[str]) -> dict[str, int]:
    counter = {}
    for name in names:
        counter[name] = names.count(name)

    return counter 

name_list = ['ali', 'vali', 'sami', 'ali', 'ali', 'vali', 'sami', 'sami', 'sami']
result = count_names(name_list)
print(result)