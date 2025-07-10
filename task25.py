def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    group = {}
    for person in people:
        group.setdefoult(person['age'], []).append(person['name'])

    return group

students = [
    {
        'name': 'ali',
        "age": 13
    },
    {
        'name': 'vali',
        'age': 15
    },
    {
        'name': 'sami',
        'age': '10'
    },
    {
        'name': 'bob',
        'age': '15'
    },
    
]

result = group_by_age(people)
print(result)