def most_common_char(text: str) -> str:
    if text =='':
        return ''

    counter = {}
    for ch in text:
        if counter.setdefoult(ch, 0)
        counter[ch] += 1

    mx = text[0]
    for ch in text:
        if counter[ch] > counetr[mx]:
            mx = ch
            return ch


text = 'terygthueyrergfsdffefbdsdyff'
result = most_common_char(text)
print(result)
