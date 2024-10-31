
class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_names in self.file_names:
            with open(file_names, encoding = 'utf-8') as files:
                line = files.read().lower()
                punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for i in punct:
                    line = line.replace(i, ' ')
                    words = line.split()
                all_words[file_names] = words
        return all_words


    def find(self, word):
        find_ = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                find_[key] = value.index(word.lower())+1
        return find_


    def count(self, word):
        count_ = {}
        for value, key in self.get_all_words().items():
            word = word.lower()
            count_[value]= key.count(word)
        return count_

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
