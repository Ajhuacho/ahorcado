class Game:

    def __init__(self, word_manager):
        self.word_man = word_manager
        print('lo primero que se ejecute')

    def play(self):
        words = self.word_man.read_words()
        print(words)
