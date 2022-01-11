import random
from ahorcado.word.word import Word


class WordManager:

    def __init__(self, words_path):
        self.path = words_path

    def get_words(self):
        with open(self.path) as f:
            words = f.read()
        words = words.split('\n')
        word_list = []
        for word in words:
            temp_word = Word(word)
            word_list.append(temp_word)
        return word_list

    def get_random_word(self):
        words = self.get_words()
        word = random.choice(words)
        return word

