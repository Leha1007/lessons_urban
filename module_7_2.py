def custom_write(file_name, strings):
    file = open(file_name, 'a')
    strings_position = {}
    for i in range(len(strings)):
        file.write(strings[i] + '\n')
        strings_position.update({(i + 1, file.tell()): strings[i]})
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
