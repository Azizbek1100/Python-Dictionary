data = {"name": "Ali", "age": 25, "city": "Tashkent"}

key = input("O'chiriladigan kalit nomini kiriting: ")

if key in data:
    del data[key]
    print(f"'{key}' kalit o'chirildi.")
else:
    print("Bunday kalit yo'q")

print(data)
