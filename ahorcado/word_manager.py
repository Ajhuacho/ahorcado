class WordManager:

    def __init__(self):
        pass

    def read_words(self):
        with open('words.txt') as f:
            words = f.read()
        return words.split('\n')