data = {
    'a': 2,
    'b': 4
}

key = input()

value = data.get(key)
if value == None:
    print("topilmadi")
else:
    print(value)