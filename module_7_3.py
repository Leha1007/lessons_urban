class WordsFinder:
    file_names = []

    def __init__(self, *file_names_str):
        for file_name in file_names_str:
            self.file_names.append(file_name)

    def get_all_words(self):
        all_words = {}
        symb_p = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file_text:
                words_list = []
                for line in file_text:
                    line.lower()
                    for ch in symb_p:
                        if ch in line:
                            line.replace(ch, ' ')
                    words_list += list(line.split())
                all_words.update({file_name: words_list})
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    find_dict.update({name: i + 1})
                    break
        return find_dict

    def count(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            s = 0
            for i in range(len(words)):
                if word.lower() == words[i]:
                    s += 1
            find_dict.update({name: s})
        return find_dict


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего