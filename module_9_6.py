def all_variants(text):
    length = len(text)
    i = 1
    for _ in range(length + 1):
        j = 0
        for __ in range(length + 1):
            if i + j <= length:
                yield text[j:j + i]
            else:
                break
            j += 1
        i += 1


a = all_variants("abc")
for i in a:
    print(i)
